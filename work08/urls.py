from django.urls import path
from . import views

urlpatterns = [
    path('', views.memo_list, name='memo_list'),
    path('new/', views.memo_new, name='memo_new'),
    path('<int:pk>/edit/', views.memo_edit, name='memo_edit'),
    path('<int:pk>/delete/', views.memo_delete, name='memo_delete'),
]
