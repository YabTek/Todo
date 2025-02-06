from django.db import models
from django.contrib.auth.models import User

# Task Model
class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="todo")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks", blank=True)
    
    def __str__(self):
        return self.title

# Checklist Model
class Checklist(models.Model):
    title = models.CharField(max_length=255)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="checklists")
    
    def __str__(self):
        return self.title