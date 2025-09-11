from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the work05 index.")

def top(request):
    return HttpResponse("This is the top page of work05.")

def list(request):
    return HttpResponse("This is the list page of work05.")

def index(request):
    return render(request, "index.html")

def index(request):
    context = {"username": "murakamiyuusei" }
    return render(request, "index.html", context)