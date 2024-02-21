from django import views
from django.urls import path
from . import views

app_name = "work"
urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("<int:id>/details", views.details, name="details"),
    
    # API URLS
    path('list/', views.TaskListView.as_view(), name='Task-list'),
    path('create/', views.create_task, name='Task-create'),
]