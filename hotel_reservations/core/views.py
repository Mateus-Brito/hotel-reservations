from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from hotel_reservations.reservation.models import Reservation


@login_required
def pannel(request):
    reservations = Reservation.objects.filter(user__id=request.user.id)
    return render(request, "pannel.html", {"reservations": reservations})


def home(request):
    return render(request, "index.html")
