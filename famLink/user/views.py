from django.shortcuts import render
from rest_framework import serializers
from .models import User
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializer import UserSerializer, UserPostSerializer

@api_view(['GET'])
def getUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postUser(request):
    name = request.data.get('name')
    email = request.data.get('email')
    gender = request.data.get('gender')
    birthday = request.data.get('birthday')
    start_working_time = request.data.get('start_working_time')
    end_working_time = request.data.get('end_working_time')
    contact = request.data.get('contact')
    user = User.objects.create(name=name,email=email,gender=gender,birthday=birthday,start_working_time=start_working_time,end_working_time=end_working_time,contact=contact)
    user.save()
    serializer = UserPostSerializer(data=request.data)
    return Response({"user_id":user.uuid})