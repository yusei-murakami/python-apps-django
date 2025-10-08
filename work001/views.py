import calendar
from datetime import date

from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Expense, Income, Category


# ホーム画面（支出と収入の一覧）
def index(request):
    expenses = Expense.objects.all().order_by("-date")
    incomes = Income.objects.all().order_by("-date")

    # 今月の収支合計
    today = date.today()
    expenses_month = expenses.filter(date__year=today.year, date__month=today.month).aggregate(Sum("amount"))["amount__sum"] or 0
    incomes_month = incomes.filter(date__year=today.year, date__month=today.month).aggregate(Sum("amount"))["amount__sum"] or 0
    balance = incomes_month - expenses_month

    context = {
        "expenses": expenses,
        "incomes": incomes,
        "expenses_month": expenses_month,
        "incomes_month": incomes_month,
        "balance": balance,
    }
    return render(request, "work001/index.html", context)


# 支出追加・編集
def expense_form(request, pk=None):
    if pk:
        expense = get_object_or_404(Expense, pk=pk)
    else:
        expense = None

    if request.method == "POST":
        date_val = request.POST["date"]
        category_id = request.POST["category"]
        amount = request.POST["amount"]
        memo = request.POST.get("memo", "")

        if expense:
            expense.date = date_val
            expense.category_id = category_id
            expense.amount = amount
            expense.memo = memo
            expense.save()
        else:
            Expense.objects.create(date=date_val, category_id=category_id, amount=amount, memo=memo)
        return redirect("work001:index")

    categories = Category.objects.filter(is_income=False)
    return render(request, "work001/expense_form.html", {"expense": expense, "categories": categories})


# 収入追加・編集
def income_form(request, pk=None):
    if pk:
        income = get_object_or_404(Income, pk=pk)
    else:
        income = None

    if request.method == "POST":
        date_val = request.POST["date"]
        category_id = request.POST["category"]
        amount = request.POST["amount"]
        memo = request.POST.get("memo", "")

        if income:
            income.date = date_val
            income.category_id = category_id
            income.amount = amount
            income.memo = memo
            income.save()
        else:
            Income.objects.create(date=date_val, category_id=category_id, amount=amount, memo=memo)
        return redirect("work001:index")

    categories = Category.objects.filter(is_income=True)
    return render(request, "work001/income_form.html", {"income": income, "categories": categories})


# 削除
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect("work001:index")


def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk)
    income.delete()
    return redirect("work001:index")


# カテゴリ管理
def category_form(request):
    if request.method == "POST":
        name = request.POST["name"]
        is_income = "is_income" in request.POST
        Category.objects.create(name=name, is_income=is_income)
        return redirect("work001:category_form")

    categories = Category.objects.all()
    return render(request, "work001/category_form.html", {"categories": categories})


# グラフ
def graph(request):
    # カテゴリ別集計
    expenses_data = Expense.objects.values("category__name").annotate(total=Sum("amount"))
    incomes_data = Income.objects.values("category__name").annotate(total=Sum("amount"))

    # 月ごとの推移
    today = date.today()
    year = today.year
    monthly_expenses = []
    monthly_incomes = []
    for month in range(1, 13):
        total_exp = Expense.objects.filter(date__year=year, date__month=month).aggregate(Sum("amount"))["amount__sum"] or 0
        total_inc = Income.objects.filter(date__year=year, date__month=month).aggregate(Sum("amount"))["amount__sum"] or 0
        monthly_expenses.append(total_exp)
        monthly_incomes.append(total_inc)

    context = {
        "expenses_data": expenses_data,
        "incomes_data": incomes_data,
        "monthly_expenses": monthly_expenses,
        "monthly_incomes": monthly_incomes,
        "months": list(range(1, 13)),
    }
    return render(request, "work001/graph.html", context)
