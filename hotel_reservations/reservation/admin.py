from django.contrib import admin
from hotel_reservations.reservation.models import Hotel, Reservation

# Register your models here.
admin.site.register([Reservation, Hotel])
