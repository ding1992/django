"""
Definition of urls for GithubStarredRepo.
"""

from datetime import datetime
from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views

import app.views
from app.models import StarredRepo

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^starredrepo$', app.views.RepoListView.as_view(),
       name='starredrepo'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^accounts/', include('allauth.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
