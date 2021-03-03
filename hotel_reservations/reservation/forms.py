from django import forms
from hotel_reservations.reservation.models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta: 
        model = Reservation