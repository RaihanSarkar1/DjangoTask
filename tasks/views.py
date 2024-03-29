from django.urls import reverse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model

from .serializers import TaskSerializer

from .models import Image, Task

# Create your views here.
def index(request):
    user = request.user.id
    tasks = Task.objects.filter(user=user).order_by('priority')
    context = {
        'tasks': tasks,
    }
    return render(request,"tasks/index.html", context)

def sortByPrio(request, id):
    user = request.user.id
    if id == 3:
        tasks = Task.objects.filter(user=user).order_by('-priority')
    elif id == 1:
        tasks = Task.objects.filter(user=user).order_by('priority')
    context = {
        'tasks': tasks,
    }
    return render(request,"tasks/index.html", context)
        

def create(request):
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        priority = request.POST['priority']
        uploaded_images = request.FILES.getlist('images')  
        print(uploaded_images)
        task = Task(title=title,description=description,due_date=date,priority=priority,user=user)
        task.save()
        for image in uploaded_images:
            # Handle upload of images
            print(image,uploaded_images)
            new_image = Image.objects.create(
                task= task,
                images = image,
            )
            
        return HttpResponseRedirect(reverse("mylist:index"),{
            'success': "Task Added Sucessfully",
        })
        
    return render(request, "tasks/create.html")



def detail(request, id):
    task = get_object_or_404(Task, pk=id)
    images = Image.objects.filter(task=task)
    return render(request, "tasks/detail.html",{
        'task': task,
        'images': images
    })
    
def delete(request, id):
    thetask = Task.objects.get(pk=id)
    thetask.delete()
    return HttpResponseRedirect('/tasks/')

def update(request, id):
    if request.method == "POST":
        task_obj = Task.objects.get(pk=id)
        task_obj.title = request.POST['title']
        task_obj.description = request.POST['description']
        task_obj.date = request.POST['date']
        task_obj.priority = request.POST['priority']
        uploaded_images = request.FILES.getlist('images')  
        task_obj.save()
        for image in uploaded_images:
            # Handle upload of images
            print(image,uploaded_images)
            new_image = Image.objects.create(
                task= task_obj,
                images = image,
            )
            
        return HttpResponseRedirect(reverse("mylist:index"),{
            'success': "Task Added Sucessfully",
        })
            
    task = Task.objects.get(pk=id)
    return render(request, "tasks/update.html", {
        'task': task,
    })

# Rest API
    
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)