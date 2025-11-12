from django.shortcuts import render

def index(request):
    return render(request, "profile.html")
def settings(request):
    return render(request, "settings.html")
