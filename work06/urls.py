from django.urls import path
from . import views

app_name = "work06"

urlpatterns = [
    path("", views.index, name="index"),
    path("reiwa/", views.reiwa, name="reiwa"),
    path("bmi/", views.bmi, name="bmi"),
    path("warikan/", views.warikan, name="warikan"),
    path("chokin/", views.chokin, name="chokin"),
    path("calculator/", views.calculator, name="calculator"),
]
