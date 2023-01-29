from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.models import User
from .models import Member
from .serializer import  AddMemberSerializer, MemberSerializer
from .memberRepository import MemberRepository
from famLink.utility import validate_request
from rest_framework import status

@api_view(['GET'])
def getMember(request):
    uuid = request.GET.get('uuid')
    try: 
        user_object = User.objects.get(uuid=uuid)
        members = Member.objects.filter(user=user_object)
        serializer = MemberSerializer(members, many=True)
    except:
        return Response({'messgae':'User does not exists'},status=400)
    return Response(serializer.data)


@api_view(['POST'])
def postMember(request):
    user_id = request.data.get('user_id')
    user = User.objects.get(uuid=user_id)
    member = Member.objects.create(priority=request.data.get('priority'),birth_day = request.data.get('birthday'),name=request.data.get('name'),ph_no=request.data.get('ph_no'),relation=request.data.get('relation'),gender=request.data.get('gender'),user=user)
    member.save()
    return Response("member added successfully")


