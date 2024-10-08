from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    psw = 'malina'
    return render(request, "generator/home.html", {'password': psw, 'title': "Personal"})
