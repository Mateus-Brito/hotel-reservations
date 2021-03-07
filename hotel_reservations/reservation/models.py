from django.db import models
from hotel_reservations.core.models import BaseModel


class Hotel(BaseModel):
    name = models.CharField("nome", max_length=255)
    description = models.TextField("descrição", max_length=512, blank=True, null=True)


class Reservation(BaseModel):
    checkin_date = models.DateField("data de check-in")
    checkout_date = models.DateField("data de check-out")
    user = models.ForeignKey(
        "auth.User",
        verbose_name="usuário",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    hotel = models.ForeignKey(
        Hotel, verbose_name="Hotel", on_delete=models.CASCADE, null=True, blank=True
    )
    room_number = models.SmallIntegerField("número do quarto")
