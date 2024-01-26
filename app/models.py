from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=50, blank=False, null = False, unique=True)
    description = models.TextField(blank=False, null=False)
    due_date = models.DateField(default = timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.title
