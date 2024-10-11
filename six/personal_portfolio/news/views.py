from django.shortcuts import render, get_object_or_404
from .models import News


def news(request):
    news = News.objects.all()
    return render(request, 'skills/index.html', {'news': news})


def zjuvopis(request):
    zjuvopis = News.objects.all()
    return render(request, 'news/zjuvopis.html', {'zjuvopis': zjuvopis})
