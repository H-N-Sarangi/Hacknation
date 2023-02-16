from django.urls import path
from .views import *

app_name = 'events'
urlpatterns = [
    # path("create/", EventCreate.as_view(), name='create'),
    path("all/", EventList.as_view(), name='all'),
    # path("<int:pk>/details/", EventList.as_view(), name='details'),
    # path("<int:pk>/update/", EventUpdate.as_view(), name='update'),
    # path("<int:pk>/delete/", EventDelete.as_view(), name='delete'),

]