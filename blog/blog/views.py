from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "index.html")

def nosotros(request):
    return render(request, "nosotros.html")