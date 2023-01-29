from django.db import models

class Coment(models.Model):
    text = models.TextField(max_length= 1000)
    username = models.CharField(max_length= 255)
    time = models.TimeField()
    date = models.DateField()
# Create your models here.
