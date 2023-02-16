from django.views.generic import TemplateView
# from .forms import OrganizerForm
from django.shortcuts import redirect, render

class HomeView(TemplateView):
    template_name='index.html'



