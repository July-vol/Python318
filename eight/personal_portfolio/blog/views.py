from django.shortcuts import render
from .models import Blog


def blogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/blogs.html', {'blogs': blogs})
