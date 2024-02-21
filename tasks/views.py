from rest_framework import generics
from django.http import HttpResponse
from django.shortcuts import render

from .serializers import TaskSerializer

from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request,"tasks/index.html", context)


def create(request):
    return render(request, "tasks/create.html")
    
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer