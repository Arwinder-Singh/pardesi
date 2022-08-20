
from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import *

# Create your models here.

class User(AbstractUser):
    username=None
    email=models.EmailField(unique=True)   
    phone_no=models.CharField(max_length=12)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    objects=UserManger()
    
class Amenities(models.Model):
    amenities_name=models.CharField(max_length=50)   
    def __str__(self):
        return self.amenities_name
    
class Room(models.Model):
    options=(
     ('category','category'),
     ('Boys','Boys',),
     ("girls",'girls'),
     ('bachelor','bachelor'),
     )
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userRoom')
    
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    category=models.CharField(max_length=20,choices=options,default='category')    
    price=models.FloatField(default=0)
    description=models.TextField()
    availablity=models.BooleanField(default=True)
    available_on=models.DateField(blank=True,null=True)
    
    
    amenities=models.ManyToManyField(Amenities)
    
class Cilent(models.Model):
     name=models.CharField(max_length=50)
     email=models.EmailField(blank=True) 
     phone_no=models.CharField(max_length=12)
        
       
class Image(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name="roomImages")
    images=models.ImageField(null=True,blank=True)