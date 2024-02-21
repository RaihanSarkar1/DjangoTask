from django.contrib import admin
from .models import Task, Image
# Register your models here.
class ImageAdmin(admin.StackedInline):
    model = Image
 
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]
 
    class Meta:
       model = Task
 
@admin.register(Image)
class TaskImageAdmin(admin.ModelAdmin):
    pass