from django.shortcuts import render
import json
                             
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
                             
from rest_framework import status
                             
from . import serializers
from . import models
import boto3
# Create your views here.
                      
@csrf_exempt
def auth_login(request):
    """Client attempts to login
                             
     - Check for username and password
     - Return serialized user data
    """
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(username=username, password=password)
                             
    if user:
        login(request,user)
        serializer = serializers.UserSerializer(user)
        args = {"user":serializer.data,"isSuccessful":1}
        return JsonResponse(args)
    return JsonResponse({"isSuccessful":0})

	
@csrf_exempt
def signup(request):
    """Client attempts to sign up
                             
     - If username does not already exist we create and authenticate new account
    """
    full_name   = request.POST['full_name']
    username    = request.POST['username']
    password    = request.POST['password']
    
    
    if models.User.objects.filter(username=username).exists():
        return JsonResponse({"isSuccessful":0})
    else:
        u = models.User(username=username)
        u.set_password(password)
        u.full_name = full_name
        u.save()
        login(request, u)
        serializer = serializers.UserSerializer(u)
        args = {"user":serializer.data,"isSuccessful":1}
        return JsonResponse(args)

@csrf_exempt
def auth_logout(request):
    """Clears the session """
    logout(request)
    return HttpResponse(status=200)


@csrf_exempt
def send_otp(request):
    # af-south-1 us-east-1
    
    phone = request.POST["phone"]
    message = request.POST["message"]
    
    client = boto3.client("sns","us-east-1")
    client.publish(PhoneNumber=phone, Message=message)
    
    args = {"isSuccessful":1,
            'phone':phone}
    
    
    return JsonResponse(args)
    
    