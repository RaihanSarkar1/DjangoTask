from django.db import models

# Create your models here.
class Task(models.Model):
    priority_choices = {
        ('LOW', 'low'),
        ('MEDIUM', 'medium'),
        ('HIGH', 'high'),
    }
    title = models.CharField(max_length=250)
    description = models.TextField()
    photos = models.FileField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=6, choices=priority_choices, default='LOW')
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Image(models.Model):
    task = models.ForeignKey(Task, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/')