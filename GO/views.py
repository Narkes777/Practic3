from django.shortcuts import render
from rest_framework import viewsets

from .models import User, Message, Сomments, Subscribers
from .serializers import MessageSerializer
# Create your views here.

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()