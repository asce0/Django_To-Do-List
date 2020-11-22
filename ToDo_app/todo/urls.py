from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<List_id>", views.delete, name="delete"),
    path("cross_off/<List_id>", views.cross_off, name="cross_off"),
    path("uncross_off/<List_id>", views.uncross_off, name="uncross_off"),
]