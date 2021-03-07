from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.shortcuts import resolve_url as r

from .forms import ReservationForm
from .models import Reservation


@login_required
def new(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)

        if not form.is_valid():
            return render(
                request,
                "new_reservation.html",
                {"form": form},
            )
        reservation = form.save(commit=False)
        reservation.user = request.user
        reservation.save()
        return redirect(r("pannel"))
    return render(
        request,
        "new_reservation.html",
        {
            "form": ReservationForm(),
        },
    )


@login_required
def delete(request, id):
    Reservation.objects.get(pk=id, user__id=request.user.id).delete()
    return redirect(r("pannel"))
