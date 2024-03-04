from django.db import models

from django.conf import settings

from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = (
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    )
    title = models.CharField(max_length=250)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(auto_now=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default='3')
    complete = models.BooleanField(default=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Image(models.Model):
    task = models.ForeignKey(Task, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')