from django import views
from django.urls import path
from . import views


app_name = "mylist"
urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("<int:id>/detail", views.detail, name="detail"),
    path("<int:id>/delete", views.delete, name="delete"),
    
    # API URLS
    path('list/', views.TaskListView.as_view(), name='Task-list'),
    path('create/', views.create_task, name='Task-create'),
]