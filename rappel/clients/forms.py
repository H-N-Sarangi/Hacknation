from django import forms
from .models import *

class EventManagerForm(forms.ModelForm):
    class Meta:
        model = EventManager 
        fields = '__all__'

       
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = '__all__'