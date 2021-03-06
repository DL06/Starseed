#from __future__ import absolute_import 
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

import datetime
from starseed.models import Project

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "index.html"

class ProductView(ListView):
      template_name = "product.html"
      model = Project


class ProfileView(DetailView):
    template_name = 'account/profile.html'
    def get_object(self):
        return get_object_or_404(get_user_model(), pk=self.request.user.id)


class ProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = 'account/profile.html'


class AddBountyView(TemplateView):
    template_name = "AddBounty.html"

class BountiesView(TemplateView):
    template_name = "bounties.html"

class DashboardView(TemplateView):
    template_name = "dashboard.html"

class MoonpieView(TemplateView):
    template_name = "moonpie.html"

class PartnersView(TemplateView):
    template_name = "partners.html"
#signup
#invte team members


from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<i>2b or !2b</i>')
