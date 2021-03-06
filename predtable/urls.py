"""predtable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from tables.views import matches_list_view, matches_list_view_base,  SearchView, model_class_view, coming_soon
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

from tables.sitemaps import StaticViewSitemap, MatchesSitemap

sitemaps = {'static': StaticViewSitemap, 'snippet': MatchesSitemap}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', matches_list_view_base, name='home'),
    path('pred/<str:abb>/', matches_list_view, name='league_tab'),
    path('', matches_list_view_base),
    path("blog/", include("blog.urls")),
    path("search/", SearchView.as_view(), name="search-view"),
    path('charts/', view=model_class_view, name='charts'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('models/', view=coming_soon, name='models'),
    path('robots.txt',  TemplateView.as_view(template_name="robots.txt", content_type='text/plain'))
#    path('pred/table/', MatchList.as_view(), name='author_table'),

 #   path("pred2/",    matches_list_view2)
]
import re
#if re.match(r"pred/(?P<league_abb>[\w-]+)/$", "pred/E0/"):
#     print("Y")


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()