from django.db import models
from clients.models import EventManager, Participants
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    image = models.ImageField(upload_to='card_imgs')
    
    def __str__(self) -> str:
        return self.name

class SubEvent(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name
    
class EventSubEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    subevent = models.ForeignKey(SubEvent, on_delete=models.CASCADE)

class ManagerEvent(models.Model):
    manager = models.ForeignKey(EventManager, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class ParticipantsSubEvent(models.Model):
    participant = models.ForeignKey(Participants, on_delete=models.CASCADE)
    subevent = models.ForeignKey(SubEvent, on_delete=models.CASCADE)