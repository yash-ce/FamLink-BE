from django.db import models
from user.models import User
# Create your models here.
import uuid

class Member(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True)
    name = models.CharField(max_length=300,blank=True,null=True)
    ph_no = models.BigIntegerField(null=True, blank=True)
    relation = models.CharField(max_length=70,null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    meta = models.JSONField(null=True, blank=True)
    is_family = models.BooleanField(null=True, blank=True) 
    is_friend = models.BooleanField(null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    nick_name = models.CharField(max_length=300,null=True, blank=True)
    birth_day = models.DateField(null=True, blank=True)
    hobbie = models.CharField(max_length=300,null=True, blank=True)
    passion = models.CharField(max_length=300,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    priority = models.IntegerField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name