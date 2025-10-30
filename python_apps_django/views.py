# index.html を表示するように変更
from django.http import HttpResponse
from django.shortcuts import render
    
def index(request):
    # return HttpResponse("Hello, world. You're at the index page.")  
    return render(request, 'index.html') 