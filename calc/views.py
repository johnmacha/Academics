from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.contrib import messages
# from django.views.generic import Objects
from .forms import ResultsForm
from .forms2 import AddPortal
from .models import Portal
from django.urls import reverse
from django.contrib.auth import login, authenticate  
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url ='/accounts/login')
def home(request):
    return render(request,'home.html')

def main(request):
    return render(request,'main.html')

def test(request):
    return render(request,'test.html')   

def tasks(request):
    return render(request,'tasks.html') 

# @login_required
# @allowed_users(allowed_roles = ['admin'])
def admins(request):
  if request.method == 'POST':
     username = request.POST.get('username')
     password = request.POST.get('password')

     user = auth.authenticate(request, username = username, password = password)
     if user is not None:
           login(request, user)
           return redirect("/")

     else:
         messages.info(request,"Invalid Credentials")
         return redirect("admins")

  else:
   return render(request, 'admin.html')

@login_required(login_url='/accounts/adminn')
# @allowed_users(allowed_roles=['ADMIN'])
def admin1(request):
    return render(request,'admin_page.html')

def admin_task(request):
    return render(request,'admin_task.html')

def marks(request): 
     forms = ResultsForm()
     if request.method == 'POST':
      forms = ResultsForm(request.POST)
      if forms.is_valid():
       forms.save()
     context = {'forms':forms}  
    
     return render(request,'award_marks.html', context)    

def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    val3 = int(request.GET['num3'])
    val4 = int(request.GET['num4'])
    val5 = int(request.GET['num5'])

    res = val1+val2+val3+val4+val5
    return render(request,'award_marks.html', {'result':res})

def profile(request):
  details = Portal.objects.all()
  return render(request, 'profile.html', {'details':details})

def profile1(request):
    forms2 = AddPortal()
    if request.method == 'POST':
        print(request.POST)
        forms2 = AddPortal(request.POST)
        if forms2.is_valid():
           forms2.save()
    context = {'forms2':forms2}    
    return render(request, 'profile1.html', context)
