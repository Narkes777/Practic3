import imp
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Message, Сomments, Subscribers
from .serializers import MessageSerializer, СommentsSerializer, SubscribersSerializer
# Create your views here.


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Message.objects.filter()
        return queryset


class СommentsViewSet(viewsets.ModelViewSet):
    serializer_class = СommentsSerializer
    queryset = Сomments.objects.all()
    permission_classes = [IsAuthenticated]


class SubscribersViewSet(viewsets.ModelViewSet):
    serializer_class = SubscribersSerializer
    queryset = Subscribers.objects.all()
    permission_classes = [IsAuthenticated]