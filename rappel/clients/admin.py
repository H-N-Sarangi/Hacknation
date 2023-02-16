from django.contrib import admin
from .models import EventManager, Participants
# Register your models here.
admin.site.register(EventManager)
admin.site.register(Participants)
