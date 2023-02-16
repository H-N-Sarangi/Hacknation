from django.urls import path
from .views import *
app_name = 'clients'
urlpatterns=[
    path("manager/", EventManagerCreateView.as_view(), name='manager'),
    path("participants/", ParticipantCreateView.as_view(), name='participant'),

]