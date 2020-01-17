# tutorial/tables.py
import django_tables2 as tables
from .models import Matches_Pred, Matches_Pred_History, Matches_Pred_Upcoming
import pandas as pd
#import django_filters


def data_corrected(**kwargs):
    corrected = kwargs.get("value", None)
    prediction = kwargs.get("value", None)
    if corrected == 1:
        return "#4ba823"
    elif corrected == 0:
        return "#d66565"
    else:
        return "#4287f5"

class Pred_Table_Summary(tables.Table):
    #corrected = tables.Column(attrs={"td": {"bgcolor": "blue"}})

    corrected = tables.Column(attrs={
        "td": {"align": "center", "bgcolor": data_corrected}
    })
    class Meta:
        model = Matches_Pred
        template_name = "django_tables2/bootstrap.html"
        fields = ("date", "HomeTeam", "AwayTeam",
                              "prediction", "Result",  "corrected" )

class Pred_Table(tables.Table):
    #corrected = tables.Column(attrs={"td": {"bgcolor": "blue"}})

    corrected = tables.Column(attrs={
        "td": {"align": "center", "bgcolor": data_corrected}
    })
    class Meta:
        model = Matches_Pred
        template_name = "django_tables2/bootstrap.html"
        fields = ("date","league", "HomeTeam", "AwayTeam", "model",
                              "prediction", "Result",  "corrected" )



class Pred_Table_Upcoming(tables.Table):
    #corrected = tables.Column(attrs={"td": {"bgcolor": "blue"}})

    class Meta:
        model = Matches_Pred_Upcoming
        template_name = "django_tables2/bootstrap.html"
        fields = ("date", "HomeTeam", "AwayTeam", "prediction", "proba")


class Pred_Table_History(tables.Table):
    #corrected = tables.Column(attrs={"td": {"bgcolor": "blue"}})

    corrected = tables.Column(attrs={
        "td": {"bgcolor":data_corrected }
    })
    class Meta:
        model = Matches_Pred_History
        template_name = "django_tables2/bootstrap.html"
        fields = ("date", "MW", "model", "HomeTeam", "AwayTeam",
                              "prediction", "Result",  "corrected" )


class MatchesTable(tables.Table):
    class Meta:
        attrs = {"class": "table table-striped table-hover cabecera-azul"}
        model = Matches_Pred_History
        fields = ("date","league", "HomeTeam", "AwayTeam", "model",
                              "prediction", "Result",  "corrected" )
        empty_text = (
            "No data to show. Try to input exact string."
        )
        template_name = "django_tables2/bootstrap.html"
        per_page = 30