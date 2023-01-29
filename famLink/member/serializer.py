from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields=('uuid','name', 'gender', 'relation','priority','ph_no',  'birth_day', )

class AddMemberSerializer(serializers.Serializer):
    relation = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True, max_length=100)
    ph_no = serializers.CharField(required=True)
    gender = serializers.IntegerField(required=True)
    age = serializers.IntegerField(required=True)
    user_id = serializers.CharField(required=True)