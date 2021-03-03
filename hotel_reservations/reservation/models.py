from django.db import models

# Create your models here.
class Reservation(models.Model):
    checkin_date = models.DateField('data de check-in')
    checkout_date = models.DateField('data de check-out')