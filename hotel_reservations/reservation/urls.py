from django.urls import path

from .views import delete, new

app_name = "reservations"

urlpatterns = [
    path("novo/", new, name="new"),
    path("<uuid:id>/delete/", delete, name="delete"),
]
