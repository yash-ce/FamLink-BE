from django.db import models
import uuid
# Create your models here.

class Sign_up(models.Model):
    uuid = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=30,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    password = models.CharField(max_length= 30,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    
class Sign_in(models.Model):
    uuid = models.IntegerField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    password = models.CharField(max_length= 30,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)



class User(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, db_index=True)
    gender = models.IntegerField(blank=True,null=True)
    name = models.CharField(max_length=40,blank=True,null=True)
    password = models.CharField(max_length=40,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    start_working_time = models.TimeField(blank=True,null=True)
    end_working_time = models.TimeField(blank=True,null=True)
    birthday = models.DateField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    contact = models.CharField(max_length=200,null=True, blank=True)
    email = models.EmailField(max_length=200, null=True,blank=True)
    status = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return self.name



    