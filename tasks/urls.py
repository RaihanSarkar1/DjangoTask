from django import views
from django.urls import path
from . import views


app_name = "mylist"
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_user, name="login"),
    path("logout", views.logout, name="logout"),
    path("signup", views.signup, name="signup"),
    path("create", views.create, name="create"),
    path("<int:id>/detail", views.detail, name="detail"),
    path("<int:id>/delete", views.delete, name="delete"),
    path("<int:id>/update", views.update, name="update"),
    
    # API URLS
    path('list/', views.TaskListView.as_view(), name='Task-list'),
    path('create/', views.create_task, name='Task-create'),
]