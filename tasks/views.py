from django.urls import reverse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .serializers import TaskSerializer

from .models import Image, Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request,"tasks/index.html", context)


def create(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        priority = request.POST['priority']
        uploaded_images = request.FILES.getlist('image')  # Replace with your actual field name
        task = Task(title=title,description=description,due_date=date,priority=priority)
        task.save()
        for image in uploaded_images:
            # Handle upload of images
            image_obj = Image(task=task,images=image)
            image_obj.save()
            
        return HttpResponseRedirect(reverse("work:index"),{
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