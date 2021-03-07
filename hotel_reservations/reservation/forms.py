from django import forms
from hotel_reservations.reservation.models import Reservation


class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["hotel"].required = True

    checkin_date = forms.DateTimeField(input_formats=["%d/%m/%Y %H:%M"])
    checkout_date = forms.DateTimeField(input_formats=["%d/%m/%Y %H:%M"])

    class Meta:
        model = Reservation
        fields = ["checkin_date", "checkout_date", "hotel", "room_number"]
