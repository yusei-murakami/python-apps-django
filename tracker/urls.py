from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
path('', views.index, name='index'),
path('add/', views.add_entry, name='add_entry'),
path('list/', views.entry_list, name='entry_list'),
path('chart/', views.chart_view, name='chart'),
path('calendar/<int:year>/<int:month>/', views.calendar_view, name='calendar'),
path('calendar/', views.calendar_redirect, name='calendar_redirect'),
]