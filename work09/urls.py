from django.urls import path
from . import views

app_name = 'work09_app'

urlpatterns = [
    path('', views.todo_list, name='list'),
    path('add/', views.todo_create, name='create'),
    path('edit/<int:pk>/', views.todo_edit, name='edit'),
    path('delete/<int:pk>/', views.todo_delete, name='delete'),
    path('toggle/<int:pk>/', views.toggle_complete, name='toggle'),
]
