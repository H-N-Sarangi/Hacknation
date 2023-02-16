from django.db import models

# Create your models here.
class EventManager(models.Model):
    username = models.CharField(max_length=50, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.username

class Participants(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    regd_no = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.fname} {self.lname}'
