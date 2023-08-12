from django.shortcuts import render, redirect
from .forms1 import SignupForm 
from .forms3 import TeachersForm
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, authenticate
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = auth.authenticate(request, username = username, password = password)
      if user is not None:
        auth.login(request, user)
        return redirect("/")
      else:
        messages.info(request, 'Invalid credentials')
        return redirect('login')
    else:        
     return render(request,'login.html')
    
def signup(request):

   forms1 = SignupForm()
   if request.method == 'POST':

    forms1 = SignupForm(request.POST)
    if forms1.is_valid():
        forms1.save()
        user = forms1.cleaned_data.get('username')
        messages.success(request, 'Your account has been created successfully for '+user)
   
        return redirect('login')
   return render(request,'signup.html', context = {'forms1':forms1})  


# def attempt(request):

# def attempt2(request):

def logout(request):
 auth.logout(request)
 return redirect("/")

def adminn(request):
   if request.method == 'POST':
      #  print(request.POST)
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = auth.authenticate(request, username = username, password = password)
       if user is not None:
            auth.login(request, user)
            return render(request,'admin_page.html')
       else:
          messages.info(request,"Invalid Credentials")
          return redirect('adminn')
    
   else:  
        return render(request,'admin.html')

def teacher(request):
   forms3 = TeachersForm()

   if request.method == 'POST':
      forms3 = TeachersForm(request.POST)

      if forms3.is_valid():
         forms3.save()

         user = forms3.cleaned_data.get('username')
         messages.success(request, 'Your account has been successfully created for '+user)

         return redirect("login")
   return render (request, 'teacher.html', context = {'forms3':forms3})   

