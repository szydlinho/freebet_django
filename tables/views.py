import pandas as pd
import numpy as np
from django.db.models import Count, Q
import json

from django.shortcuts import render
from django.http import Http404
from django_tables2 import SingleTableView

from django.shortcuts import render, get_object_or_404
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import MatchesListFilter
import pandas as pd
import numpy as np

# Create your views here.

from .models import Matches_Pred, Matches_Pred_History, Matches_Pred_Upcoming
from .tables import Pred_Table, Pred_Table_Summary, Pred_Table_History, Pred_Table_Upcoming


def matches_list_view(request, abb):

    table_vc_bef = Matches_Pred_History.objects.filter(league=str(abb), model='ECL').order_by('-MW', '-date')
    table_vc_bef_df = pd.DataFrame(list(table_vc_bef.values()))
    table_vc_bef_df.replace('', np.nan, inplace=True)
    acc_vc = np.mean(table_vc_bef_df['corrected'])

    table_vc = Pred_Table_History(table_vc_bef)
    table_vc.paginate(page=request.GET.get("page", 1), per_page=10)

    table_lr_bef = Matches_Pred_History.objects.filter(league=str(abb), model='LR').order_by('-MW', '-date')
    table_lr_bef_df = pd.DataFrame(list(table_lr_bef.values()))
    table_lr_bef_df.replace('', np.nan, inplace=True)
    acc_lr = np.mean(table_lr_bef_df['corrected'])
    table_lr = Pred_Table_History(table_lr_bef)
    table_lr.paginate(page=request.GET.get("page", 1), per_page=10)

    table_dt_bef = Matches_Pred_History.objects.filter(league=str(abb), model='DT').order_by('-MW', '-date')
    table_dt_bef_df = pd.DataFrame(list(table_dt_bef.values()))
    table_dt_bef_df.replace('', np.nan, inplace=True)
    acc_dt = np.mean(table_dt_bef_df['corrected'])
    table_dt = Pred_Table_History(table_dt_bef)
    table_dt.paginate(page=request.GET.get("page", 1), per_page=10)


    return render(request, "table.html", {
        "table_vc": table_vc, "acc_vc" : acc_lr, "acc_lr" : acc_lr, "acc_dt" : acc_dt, "table_lr":table_lr, "table_dt": table_dt
    })

def matches_list_view_base(request):


    tablee0 = Pred_Table_Upcoming(Matches_Pred_Upcoming.objects.filter(league='E0', model='ECL').order_by('-MW', 'date')[:10])
    tabled1 = Pred_Table_Upcoming(Matches_Pred_Upcoming.objects.filter(league='D1', model='ECL').order_by('-MW', 'date')[:10])
    tablesp1 = Pred_Table_Upcoming(Matches_Pred_Upcoming.objects.filter(league='SP1', model='ECL').order_by('-MW', 'date')[:10])
    tablei1 = Pred_Table_Upcoming(Matches_Pred_Upcoming.objects.filter(league='I1', model='ECL').order_by('-MW', 'date')[:10])
    tablef1 = Pred_Table_Upcoming(Matches_Pred_Upcoming.objects.filter(league='F1', model='ECL').order_by('-MW', 'date')[:10])
    tablee1 = Pred_Table_Upcoming(Matches_Pred_Upcoming.objects.filter(league='E1', model='ECL').order_by('-MW', 'date')[:12])
    #table.paginate(page=request.GET.get("page", 1), per_page=10)
    return render(request, "all_tables.html", {
        "tablee0": tablee0, "tabled1":tabled1, "tablesp1": tablesp1, "tablei1": tablei1, "tablef1":tablef1, "tablee1":tablee1
    })


class SearchView(SingleTableMixin, FilterView):
    model = Matches_Pred_History
    table_class = Pred_Table_History
    template_name = "template.html"
    filter_class = MatchesListFilter



def model_class_view(request):
    dataset = Matches_Pred_History.objects \
        .values('model') \
        .annotate(corrected_count=Count('model', filter=Q(corrected=1)),
                  not_corrected_count=Count('model', filter=Q(corrected=0))) \
        .order_by('corrected_count')

    categories = list()
    corrected_series = list()
    not_corrected_series = list()

    for entry in dataset:
        categories.append(entry['model'])
        corrected_series.append(entry['corrected_count'])
        not_corrected_series.append(entry['not_corrected_count'])

    dataset_league = Matches_Pred_History.objects \
        .values('league') \
        .annotate(corrected_count_l=Count('league', filter=Q(corrected=1)),
                  not_corrected_count_l=Count('league', filter=Q(corrected=0))) \
        .order_by('corrected_count_l')

    categories_l = list()
    corrected_series_l = list()
    not_corrected_series_l = list()

    for entry in dataset_league:
        categories_l.append( entry['league'])
        corrected_series_l.append(entry['corrected_count_l'])
        not_corrected_series_l.append(entry['not_corrected_count_l'])


    dataset_prc = Matches_Pred_History.objects.reverse()
    dataset_prc_df = pd.DataFrame(list(dataset_prc.values()))
    dataset_prc_df.replace('', np.nan, inplace=True)
    dataset_prc_df = dataset_prc_df.groupby(['model', 'corrected']).agg({'corrected': 'count'})

    dataset_prc_df = dataset_prc_df.groupby(level=0).apply(lambda x: 100 * x / float(x.sum()))
    dataset_prc_df.columns = ["corrected_prc"]
    dataset_prc_df.reset_index(inplace= True)
    dataset_prc_df = dataset_prc_df.loc[dataset_prc_df.corrected == 1]
    dataset_prc_df = dataset_prc_df.sort_values('corrected_prc')
    dataset_prc_df = dataset_prc_df[['model', 'corrected_prc']]
    dataset_prc_df.corrected_prc = dataset_prc_df.corrected_prc.round(2)
    dataset_prc_json = dataset_prc_df.to_json(orient='records')
    dataset_prc_json = json.loads(dataset_prc_json)

    categories_prc = list()
    corrected_prc = list()

    for entry in dataset_prc_json:
        categories_prc.append(entry['model'])
        corrected_prc.append(entry['corrected_prc'])


    return render(request, 'model.html', {
        'categories': json.dumps(categories),
        'corrected_series': json.dumps(corrected_series),
        'not_corrected_series': json.dumps(not_corrected_series),
        'categories_l': json.dumps(categories_l),
        'corrected_series_l': json.dumps(corrected_series_l),
        'not_corrected_series_l': json.dumps(not_corrected_series_l),
        'categories_prc': json.dumps(categories_prc),
        'corrected_prc': json.dumps(corrected_prc)
    })


def detail(request, abb=None):
    league = get_object_or_404(Matches_Pred.objects.values('league').distinct(), abb=abb)

    return render(request,
                  'pred/detail.html',
                  {'league': league})


def coming_soon(request):
    return render(request,'coming_soon.html')