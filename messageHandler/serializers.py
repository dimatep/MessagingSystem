from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User

# class's that going to convert the Message and User model to JSON data


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(slug_field='username', many=False, queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(slug_field='username', many=False, queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ('sender', 'receiver', 'subject', 'message', 'creation_date')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

