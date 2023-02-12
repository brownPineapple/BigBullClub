from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Booking(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField('Date of booking')
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    amount = models.IntegerField()