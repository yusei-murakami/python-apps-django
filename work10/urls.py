# work10/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'work10'

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('add/', views.TodoCreateView.as_view(), name='todo_add'),
    path('edit/<int:pk>/', views.TodoUpdateView.as_view(), name='todo_edit'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='todo_delete'),

    # registration
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
