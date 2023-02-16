from django import forms
from .models import Event, SubEvent

class  EventForm(forms.Form):
    name = forms.CharField(max_length=50)
    # description 