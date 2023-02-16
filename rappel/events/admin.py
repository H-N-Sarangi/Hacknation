from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Event)
admin.site.register(SubEvent)
admin.site.register(EventSubEvent)
admin.site.register(ManagerEvent)
admin.site.register(ParticipantsSubEvent)


