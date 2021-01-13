from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from accounts.models import Account


class Organization(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(Account)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS = [
        ('Created','Created'),
        ('Pending','Pending'),
        ('Completed','Completed'),
    ]
    title = models.CharField(max_length=300)
    assignee =models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Created')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(Account)

    
    def __str__(self):
        return self.title