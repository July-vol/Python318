from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name="news"),
    path('news/', views.zjuvopis, name="zjuvopis"),
]
