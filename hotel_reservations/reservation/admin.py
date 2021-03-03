from django.contrib import admin
from hotel_reservations.reservation.models import Reservation

# Register your models here.
admin.site.register([Reservation])