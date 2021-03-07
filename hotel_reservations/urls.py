from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("hotel_reservations.core.urls")),
    path(
        "painel/reservas/",
        include("hotel_reservations.reservation.urls"),
    ),
]
