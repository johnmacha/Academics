from django.urls import path 
from . import views

urlpatterns = [

    path('login', views.login, name='login'),
    path('signup', views.signup, name = 'signup'),
    path('logout', views.logout, name='logout'),
    path('adminn', views.adminn, name='adminn'),
    path('teacher', views.teacher, name = 'teacher'),
]