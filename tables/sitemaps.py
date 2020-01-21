from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from tables.models import  Matches_Pred_History


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['home', 'search-view', 'charts']

    def location(self, item):
        return reverse(item)


class MatchesSitemap(Sitemap):

    def items(self):
        query = "SELECT * FROM tables_matches_pred_history WHERE date = (SELECT MAX(date) FROM " \
                "tables_matches_pred_history " \
                "AS f WHERE f.league = tables_matches_pred_history.league) AND model = 'LR' and prediction = 1 "
        return  Matches_Pred_History.objects.raw(query)