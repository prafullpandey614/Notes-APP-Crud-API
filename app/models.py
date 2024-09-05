from turtle import update
from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"
    