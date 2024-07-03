from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
 

class Message(models.Model):
       Value = models.CharField(max_length=100000)
       user = models.CharField(max_length=100000)
       Room = models.CharField(max_length=100000)
       date = models.DateTimeField(default=datetime.now, blank=True)