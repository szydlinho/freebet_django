from django.shortcuts import render
from django.forms.utils import flatatt
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import MatchesListFilter
import pandas as pd
import numpy as np

# Create your views here.

from .models import Matches_Pred, Matches_Pred_History, Matches_Pred_Upcoming
from .tables import Pred_Table, Pred_Table_Summary, Pred_Table_History, Pred_Table_Upcoming


def matches_list_view(request, abb):

    table_vc_bef = Matches_Pred_History.objects.filter(league=str(abb), model='ECL').reverse()[:50]
    table_vc_bef_df = pd.DataFrame(list(table_vc_bef.values()))
    table_vc_bef_df.replace('', np.nan, inplace=True)
    acc_vc = np.mean(table_vc_bef_df['corrected'])

    table_vc = Pred_Table_History(table_vc_bef)
    table_vc.paginate(page=request.GET.get("page", 1), per_page=10)

    table_lr_bef = Matches_Pred_History.objects.filter(league=str(abb), model='LR').reverse()[:50]
    table_lr_bef_df = pd.DataFrame(list(table_lr_bef.values()))
    table_lr_bef_df.replace('', np.nan, inplace=True)
    acc_lr = np.mean(table_lr_bef_df['corrected'])
    table_lr = Pred_Table_History(table_lr_bef)
    table_lr.paginate(page=request.GET.get("page", 1), per_page=10)

    table_dt_bef = Matches_Pred_History.objects.filter(league=str(abb), model='DT').reverse()[:50]
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
    model = Matches_Pred
    table_class = Matches_Pred
    template_name = "template.html"
    filter_class = MatchesListFilter