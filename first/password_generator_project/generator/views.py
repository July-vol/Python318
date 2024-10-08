from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   psw = 'qwerty'
   return render(request, 'generator/home.html', {'password': psw, 'title': "First page"})
