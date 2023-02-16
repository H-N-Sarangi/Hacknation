from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Event, SubEvent
from .forms import *
from django.urls import reverse_lazy
# Create your views here.
class EventList(ListView):
    model = Event
    template_name = 'events/event_list.html'

class EventDetails(DetailView):
    model = Event
    template_name = 'events/event_details.html'

@login_required
def create_event(request):
    pass


# class EventCreate(LoginRequiredMixin, CreateView):
#     model = Event
#     form_class = EventForm
#     template_name = 'events/event_form.html'
#     success_url = reverse_lazy('homepage')

# class EventUpdate(LoginRequiredMixin, UpdateView):
#     model = Event
#     fields='__all__'
#     template_name = 'events/event_form.html'
#     success_url = reverse_lazy('homepage')

# class EventDelete(LoginRequiredMixin, DeleteView):
#     model = Event
#     template_name = 'events/event_delete.html'
#     success_url = reverse_lazy('homepage')
