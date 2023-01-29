from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('uuid','name','email', 'gender', 'birthday', 'start_working_time', 'end_working_time', 'contact')

class UserPostSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True, max_length=100)
    contact = serializers.CharField(required=True)
    gender = serializers.IntegerField(required=True)

