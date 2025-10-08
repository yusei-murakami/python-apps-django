from django.urls import path
from . import views

app_name = "work07"

urlpatterns = [
    path("", views.index, name="index"),
    path("omikuji/", views.omikuji, name="omikuji"),
    path("janken/", views.janken, name="janken"),
    path("highlow/", views.highlow, name="highlow"),
]
