from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="blogs"),
    path(r'<?Pint:blog_id>\[0-9]+)/$', views.detail, name='detail'),
]
