from django.apps import AppConfig


class Work06Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'work06'

from django.shortcuts import render

# --- 西暦↔和暦 ---
def reiwa(request):
    result = None
    if request.method == "POST":
        year = request.POST.get("year")
        era = request.POST.get("era")
        # 西暦→和暦
        if year and year.isdigit():
            year = int(year)
            if year >= 2019:
                result = f"令和{year - 2018}年"
            elif year >= 1989:
                result = f"平成{year - 1988}年"
            elif year >= 1926:
                result = f"昭和{year - 1925}年"
            else:
                result = "対象外の年です"
        # 和暦→西暦
        elif era:
            import re
            match = re.match(r"(令和|平成|昭和)(\d+)年", era)
            if match:
                gengo, num = match.groups()
                num = int(num)
                if gengo == "令和":
                    result = 2018 + num
                elif gengo == "平成":
                    result = 1988 + num
                elif gengo == "昭和":
                    result = 1925 + num
                else:
                    result = "対象外の元号です"
            else:
                result = "形式が正しくありません（例：令和5年）"
    return render(request, "work06/reiwa.html", {"result": result})

# --- トップページ ---
def index(request):
    return render(request, "work06/index.html")

# --- BMI計算 ---
def bmi(request):
    result = None
    if request.method == "POST":
        weight = request.POST.get("weight")
        height = request.POST.get("height")
        if weight and height:
            try:
                weight = float(weight)
                height = float(height) / 100  # cm → m
                result = round(weight / (height ** 2), 2)
            except:
                result = "数値を入力してください"
    return render(request, "work06/bmi.html", {"result": result})

# --- 割り勘計算 ---
def warikan(request):
    result = None
    if request.method == "POST":
        total = request.POST.get("total")
        people = request.POST.get("people")
        if total and people:
            try:
                total = float(total)
                people = int(people)
                if people == 0:
                    result = "人数は1以上で入力してください"
                else:
                    result = round(total / people, 2)
            except:
                result = "数値を入力してください"
    return render(request, "work06/warikan.html", {"result": result})

# --- 貯金計算 ---
def chokin(request):
    result = None
    if request.method == "POST":
        monthly = request.POST.get("monthly")
        years = request.POST.get("years")
        if monthly and years:
            try:
                monthly = float(monthly)
                years = int(years)
                result = []
                for y in range(1, years+1):
                    result.append((y, monthly*12*y))
            except:
                result = "数値を入力してください"
    return render(request, "work06/chokin.html", {"result": result})

# --- 四則演算計算機 ---
def calculator(request):
    result = None
    if request.method == "POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        op = request.POST.get("operator")
        if num1 and num2:
            try:
                num1 = float(num1)
                num2 = float(num2)
                if op == "+":
                    result = num1 + num2
                elif op == "-":
                    result = num1 - num2
                elif op == "*":
                    result = num1 * num2
                elif op == "/":
                    if num2 == 0:
                        result = "0で割れません"
                    else:
                        result = num1 / num2
            except:
                result = "数値を入力してください"
    return render(request, "work06/calculator.html", {"result": result})
