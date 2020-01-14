from django.shortcuts import render

# Create your views here.

from .models import Matches_Pred, Matches_Pred_History, Matches_Pred_Upcoming
from .tables import Pred_Table, Pred_Table_Summary, Pred_Table_History, Pred_Table_Upcoming


def matches_list_view(request, abb):

    table = Pred_Table_History(Matches_Pred_History.objects.filter(league=str(abb)).order_by('-MW', 'date'))
    table.paginate(page=request.GET.get("page", 1), per_page=10)
    return render(request, "table.html", {
        "table": table
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


