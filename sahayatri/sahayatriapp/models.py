from contextlib import nullcontext
from dataclasses import asdict
from distutils.command.upload import upload
import email
from email.mime import image
from importlib.abc import TraversableResources
from itertools import product
from operator import mod
from pyexpat import model
from re import T
from statistics import mode
from telnetlib import STATUS
from tkinter import CASCADE
from tkinter.tix import Tree
from unicodedata import category, name
from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth.models import User,AbstractUser


# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=250,null=True)
    description=models.TextField(null=True)
    email=models.EmailField(max_length=100,null=True)
    phone=models.BigIntegerField(null=True)
    logo=models.ImageField(upload_to="static/img/")
    bgimage=models.ImageField(upload_to="static/img/")
    
    def __str__(self):
        return self.name
class Province(models.Model):
    name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

class District(models.Model):
    name=models.CharField(max_length=100,null=True)
    province=models.ForeignKey(Province,related_name='province',max_length=100,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Municipality(models.Model):
    name=models.CharField(max_length=100,null=True)
    district=models.ForeignKey(District,related_name='district',max_length=100,null=True,on_delete=models.CASCADE)    
    def __str__(self):
        return self.name

class BudgetCategory(models.Model):
    name=models.CharField(max_length=250,null=True)
    startPrice=models.BigIntegerField(null=True)
    endPrice=models.BigIntegerField(null=True)
    status=models.BooleanField(default=True,null=True)

    def __str__(self):
        return self.name
    
class TypeCategory(models.Model):
    name=models.CharField(max_length=250,null=True,unique=True)
    status=models.BooleanField(default=True,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):    
    name = models.CharField(max_length=200,null=True)
    price =models.CharField(max_length=10,null=True)
    category=models.ForeignKey(TypeCategory,related_name='cat',on_delete=models.CASCADE,null=True)
    budget=models.ForeignKey(BudgetCategory,related_name='bud',on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='media',null=True)
    description = models.CharField(max_length=5000,null=True,blank=True)
    posted_by = models.ForeignKey(User,related_name='author',null=True,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status=models.BooleanField(default=False)
    inclusions=models.TextField(null=True)
    exclusions=models.TextField(null=True)
    mapurl=models.URLField(null=True)
    days=models.IntegerField(null=True,default=1)
    nights=models.IntegerField(null=True)
    province=models.ForeignKey(Province,related_name='prov0',on_delete=models.CASCADE,null=True)
    district=models.ForeignKey(District,related_name='district0',on_delete=models.CASCADE,null=True)
    muni=models.ForeignKey(Municipality,related_name='muni0',on_delete=models.CASCADE,null=True)
    discount=models.DecimalField(null=True,max_digits=10,decimal_places=2)
    newprice=models.DecimalField(null=True,max_digits=10,decimal_places=2)
    featured=models.BooleanField(default=False)
    Itnerary=models.TextField(null=True)
    entrydate=models.DateTimeField(auto_now_add=True,null=True)
    valid_date=models.DateTimeField(null=True)
    offers=models.CharField(max_length=250,null=True,default='N/A')
    overview=models.TextField(null=True)
    image1=models.ImageField(upload_to='media',null=True)
    image2=models.ImageField(upload_to='media',null=True)
    image3=models.ImageField(upload_to='media',null=True)
    image4=models.ImageField(upload_to='media',null=True)
    avg_rating=models.DecimalField(null=True,max_digits=3,decimal_places=2)

    def __str__(self):
        return self.name



class Merchant(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    email=models.CharField(max_length=100,null=True)
    fullname=models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=200,null=True)
    type_of_user = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    country = models.CharField(max_length=200,default='Nepal',null=True)
    province=models.ForeignKey(Province,related_name='prov2',on_delete=models.CASCADE,null=True)
    district=models.ForeignKey(District,related_name='district2',on_delete=models.CASCADE,null=True)
    muni=models.ForeignKey(Municipality,related_name='muni2',on_delete=models.CASCADE,null=True)
    age = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200,null=True)
    pan_no = models.CharField(max_length=200,null=True)
    company_name = models.CharField(max_length=200,null=True)
    company_website = models.URLField(max_length=200,null=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.fullname


class Customer(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    fullname=models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=20,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    type_of_user = models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=100,null=True)
    #categories = models.CharField(max_length=200,null=True,choices=Product.CATEGORY)
    country = models.CharField(max_length=200,default='Nepal',null=True)
    province=models.ForeignKey(Province,related_name='prov1',on_delete=models.CASCADE,null=True)
    district=models.ForeignKey(District,related_name='district1',on_delete=models.CASCADE,null=True)
    muni=models.ForeignKey(Municipality,related_name='muni1',on_delete=models.CASCADE,null=True)
    age = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200,null=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.fullname

class Slider(models.Model):
    alttext1=models.CharField(max_length=100,null=True)
    alttext2=models.CharField(max_length=100,null=True)
    alttext3=models.CharField(max_length=100,null=True)
    sliderimg=models.ImageField(upload_to="static/img/")
    status=models.BooleanField(default=True)

# class Overview(models.Model):
#     product=models.ForeignKey(Product,related_name='+',on_delete=models.CASCADE,null=True)
#     author=models.ForeignKey(Merchant,on_delete=models.CASCADE,null=True)
#     facts=models.TextField(null=True)
#     travelinfo=models.TextField(null=True)
#     status=models.BooleanField(default=True)

class Itnerary(models.Model):
    product=models.ForeignKey(Product,related_name='itner',on_delete=models.CASCADE,null=True)
    author=models.ForeignKey(Merchant,on_delete=models.CASCADE,null=True)
    day=models.CharField(max_length=250,default='Day 1',null=True)
    detail=models.TextField(null=True)
    travel=models.TextField(null=True)
    breakfast=models.TextField( null=True)
    lunch=models.TextField(null=True)
    dinner=models.TextField(null=True)
    accomodation=models.TextField(null=True)
    sighting=models.TextField(null=True)
    extra=models.TextField(null=True)
    status=models.BooleanField(default=True)



class ImageCollection(models.Model):
    product=models.ForeignKey(Product,related_name='img',on_delete=models.CASCADE,null=True)
    author=models.ForeignKey(Merchant,on_delete=models.CASCADE,null=True)
    image1=models.ImageField(upload_to='media')
    image2=models.ImageField(upload_to='media')
    image3=models.ImageField(upload_to='media')
    image4=models.ImageField(upload_to='media')

class Rating(models.Model):
    item=models.ForeignKey(Product,related_name='prod_rate',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='rated_by',on_delete=models.CASCADE)
    rating=models.IntegerField(default=0,null=True)

class Bucketlist(models.Model):
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    posted_by=models.IntegerField(null=True)
    
class Order(models.Model):
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    total=models.CharField(max_length=100,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    refId = models.CharField(max_length=250,null=True)
    posted_by = models.CharField(max_length=100,null=True)
    payment=models.CharField(max_length=100,null=True)

    


