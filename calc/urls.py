from django.urls import path
from . import views
# from .views import RestrictMembers

app_name = 'calc'

urlpatterns = [
    path('',views.home, name='home'),
    path('main/', views.main, name='main'),
    path('test', views.test, name='test'),
    path('tasks/', views.tasks, name='tasks'),
    path('admins/', views.admins, name='admins'),
    path('admin1/', views.admin1, name='admin1'),
    path('admin_task/',views.admin_task, name='admin_task' ),
    path('marks/', views.marks, name ='marks'),
    path('add/', views.add, name='add'),
    path('profile/', views.profile, name='profile'),
    path('profile1/', views.profile1, name='profile1'),

]