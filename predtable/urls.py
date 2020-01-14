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
from tables.views import matches_list_view, matches_list_view_base




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', matches_list_view_base, name='home'),
    path('pred/<str:abb>/', matches_list_view, name='league_tab'),
    path('', matches_list_view_base),
    path("blog/", include("blog.urls")),

#    path('pred/table/', MatchList.as_view(), name='author_table'),

 #   path("pred2/",    matches_list_view2)
]
import re
#if re.match(r"pred/(?P<league_abb>[\w-]+)/$", "pred/E0/"):
#     print("Y")

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
