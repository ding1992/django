"""
Definition of views.
"""

from app.models import StarredRepo
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests

class RepoListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/github/login/?process=login'
    model = StarredRepo
    context_object_name = 'starredrepo_list'
    template_name = 'app/starredrepo.html'

    def get_queryset(self):
        reposList = []
        if self.request.user.is_authenticated:
            r = requests.get('https://api.github.com/users/'+self.request.user.username+'/starred')
            repos = r.json()
            
            for repo in repos:
                reposList.append(StarredRepo(repo))

        return reposList

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )