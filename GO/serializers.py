from rest_framework import serializers
from .models import Message, Сomments, Subscribers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class СommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сomments
        fields = '__all__'


class SubscribersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribers
        fields = '__all__'