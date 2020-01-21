from django.contrib import admin

# Register your models here.
from tables.models import Matches_Pred, Matches_Pred_Upcoming, Matches_Pred_History
from django.contrib.sites.models import Site

admin.site.register(Matches_Pred_History)