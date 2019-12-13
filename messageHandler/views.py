from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Message
from . serializers import MessageSerializer
from . serializers import UserSerializer

# Create your views here.
# here I define what should the users see when they navigate to certain page

# /messages
@csrf_exempt
def list_of_messages(request, sender=None, receiver=None):
    # GET Request
    # get the list of all the messages
    if request.method == 'GET':
        message = Message.objects.filter(sender_id=sender, receiver_id=receiver)
        serializer = MessageSerializer(message, context={'request': request}, many=True)
        return JsonResponse(serializer.data, safe=False)

    # create a new message and add it to the existing list
    # POST Request
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        serializer = MessageSerializer(data=request_data)
        if serializer.is_valid():   # if valid then save the data
            serializer.save()
            return JsonResponse(serializer.data, status=201)    # resource is created inside a collection
        return JsonResponse(serializer.errors, status=400)      # BAD REQUEST - The client SHOULD NOT repeat the request without modifications

# /users
@csrf_exempt
def list_of_users(request, id_primary_key=None):
    # GET Request
    if request.method == 'GET':
        if id_primary_key:
            users = User.objects.filter(id=id_primary_key)
        else:
            users = User.objects.all()
        serializer = UserSerializer(users, context={'request': request}, many=True)
        return JsonResponse(serializer.data, safe=False)

    # POST Request
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        serializer = MessageSerializer(data=request_data)
        if serializer.is_valid():   # if valid then save the data
            serializer.save()
            return JsonResponse(serializer.data, status=201)    # resource is created inside a collection
        return JsonResponse(serializer.errors, status=400)      # BAD REQUEST - The client SHOULD NOT repeat the request without modifications

