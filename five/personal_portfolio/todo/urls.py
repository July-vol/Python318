
from django.urls import path
from todo import views

urlpatterns = [

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    # Todos
    path('current', views.currenttodos, name='currenttodos'),
    path('create/', views.createtodo, name='createtodo'),
    path('', views.home, name='home'),
    path('todo/<int:todo_pk>/', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),

]
