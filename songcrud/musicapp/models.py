from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.
class artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

class song(models.Model):
    title = models.CharField(max_length=50)
    date_released= models.DateField(default=datetime.today)
    likes = models.IntegerField()
    # ariste_id=

class lyric(models.Model):
    content = models.CharField(max_length=1500)
    # song_id=
 