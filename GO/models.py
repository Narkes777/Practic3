from email import message
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model): # user = User.objects.first(); user.likes.all()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')

class Сomments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    
class Subscribers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(User, related_name='subscribtions')