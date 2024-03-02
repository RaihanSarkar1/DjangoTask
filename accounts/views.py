from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from tasks.models import Task
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm



# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('mylist:index')
        else:
            messages.success(request,("There was a problem logging in, Try Again.."))
            return render(request,"accounts/login.html")
    else:
        return render(request,"accounts/login.html")
    
        


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("mylist:index"),{
            'success': "Logged out Sucessfully",
        })
    
def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        
        
            
            return HttpResponseRedirect(reverse("account:login"),{
            'success': "Registration Successful. Login to continue.",
            })
        
        
    return render(request,"accounts/signup.html", {
        'form': form,
    })
