from django.urls import path
from . import views

app_name = "work001"

urlpatterns = [
    path("", views.index, name="index"),
    path("expense/add/", views.expense_form, name="expense_add"),
    path("expense/edit/<int:pk>/", views.expense_form, name="expense_edit"),
    path("expense/delete/<int:pk>/", views.delete_expense, name="expense_delete"),
    path("income/add/", views.income_form, name="income_add"),
    path("income/edit/<int:pk>/", views.income_form, name="income_edit"),
    path("income/delete/<int:pk>/", views.delete_income, name="income_delete"),
    path("categories/", views.category_form, name="category_form"),
    path("graph/", views.graph, name="graph"),
]
