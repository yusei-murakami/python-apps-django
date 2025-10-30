import google.generativeai as genai
import os
from django.http import HttpResponse

def simple_qa(request):
    # query stringから質問を取得
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    question = request.GET.get("question", "おすすめのレシピは？")

    model = genai.GenerativeModel("gemini-2.0-flash")  # または 'gemini-pro'

    prompt = "質問: {question}\n回答:".format(question=question)

    print(f"送信するプロンプト: {prompt}\n")

    # テキスト生成を実行
    response = model.generate_content(prompt)

    return HttpResponse(f"<pre>{response.text}</pre>")





# ここにアクセス: http://127.0.0.1:8000/work11/simple_qa/?question=%E3%83%86%E3%82%B9%E3%83%88