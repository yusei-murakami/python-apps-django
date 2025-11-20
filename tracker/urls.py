from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_measurement, name='add_measurement'),
    path('measurement/<int:pk>/', views.view_measurement, name='view_measurement'),
    path('api/calendar/', views.api_calendar, name='api_calendar'),
    path('api/charts/', views.api_charts, name='api_charts'),
]
