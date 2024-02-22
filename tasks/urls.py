from django import views
from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

app_name = "MyTM"
urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("<int:id>/detail", views.detail, name="detail"),
    
    # API URLS
    path('list/', views.TaskListView.as_view(), name='Task-list'),
    path('create/', views.create_task, name='Task-create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)