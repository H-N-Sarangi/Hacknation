from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.views.generic import CreateView
# Create your views here.
class EventManagerCreateView(CreateView):
    model = EventManager
    form_class = EventManagerForm
    template_name = 'clients/registration.html'
    success_url = reverse_lazy('homepage')

class ParticipantCreateView(CreateView):
    model = Participants
    form_class = ParticipantForm
    template_name = 'clients/registration.html'
    success_url = reverse_lazy('homepage')
