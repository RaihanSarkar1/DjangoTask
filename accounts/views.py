from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from tasks.models import Task
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect



# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            tasks = Task.objects.all()
            context = {
                'tasks': tasks,
            }
            return render(request,"tasks/index.html", context)
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
    return render(request,"accounts/signup.html")
