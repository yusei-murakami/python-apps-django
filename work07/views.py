from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import random

# トップページ
def index(request):
    return render(request, 'work07/index.html')

# おみくじ
def omikuji(request):
    results = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    # ボタン押したときはランダムに選択
    result = random.choice(results)
    return render(request, 'work07/omikuji.html', {'result': result})

# じゃんけん
def janken(request):
    choices = ["グー", "チョキ", "パー"]
    user_choice = request.GET.get('choice')
    cpu_choice = random.choice(choices)
    result = ""
    if user_choice:
        if user_choice == cpu_choice:
            result = "あいこ"
        elif (user_choice == "グー" and cpu_choice == "チョキ") or \
             (user_choice == "チョキ" and cpu_choice == "パー") or \
             (user_choice == "パー" and cpu_choice == "グー"):
            result = "勝ち"
        else:
            result = "負け"
    return render(request, 'work07/janken.html', {
        'choices': choices,
        'user_choice': user_choice,
        'cpu_choice': cpu_choice,
        'result': result
    })

# Hi & Low
def highlow(request):
    user_choice = request.GET.get('choice')
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    result = ""
    if user_choice:
        if (user_choice == "High" and num2 > num1) or \
           (user_choice == "Low" and num2 < num1):
            result = "正解！"
        else:
            result = "不正解"
    return render(request, 'work07/highlow.html', {
        'num1': num1,
        'num2': num2,
        'user_choice': user_choice,
        'result': result
    })
