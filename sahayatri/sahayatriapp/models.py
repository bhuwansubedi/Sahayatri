from dataclasses import asdict
from distutils.command.upload import upload
from email.mime import image
from itertools import product
from operator import mod
from pyexpat import model
from re import T
from statistics import mode
from telnetlib import STATUS
from tkinter import CASCADE
from tkinter.tix import Tree
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User

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


class Product(models.Model):
    CATEGORY = (
        ('Hiking','Hiking'),
        ('Heritage','Heritage'),
        ('Historical','Historical'),
        ('Nature','Nature'),
        ('Camping','Camping'),
        ('Rafting','Rafting'),
        ('Safari','Safari'),
        ('Trekking','Trekking'),
        ('Sightseeing','Sightseeing'),
        ('Misc.','Misc.')
    )

    name = models.CharField(max_length=200,null=True)
    price =models.CharField(max_length=10,null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    image = models.ImageField(upload_to='media',null=True)
    description = models.CharField(max_length=5000,null=True,blank=True)
    posted_by = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Merchant(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
        ('Rather not specify','Rather not specify'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=200,null=True)
    type_of_user = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    country = models.CharField(max_length=200,null=True)
    province = models.CharField(max_length=200,null=True)
    district = models.CharField(max_length=200,null=True)
    municipality = models.CharField(max_length=200,null=True)
    age = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200,null=True,choices=GENDER)
    pan_no = models.CharField(max_length=200,null=True)
    company_name = models.CharField(max_length=200,null=True)
    company_website = models.CharField(max_length=200,null=True)
    status=models.BooleanField(default=False)


    def __str__(self):
        return self.username


class Customer(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
        ('Rather not specify','Rather not specify'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=20,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    type_of_user = models.CharField(max_length=200,null=True)
    categories = models.CharField(max_length=200,null=True,choices=Product.CATEGORY)
    country = models.CharField(max_length=200,null=True)
    province = models.CharField(max_length=200,null=True)
    district = models.CharField(max_length=200,null=True)
    municipality = models.CharField(max_length=200,null=True)
    age = models.CharField(max_length=200,null=True)
    gender = models.CharField(max_length=200,null=True,choices=GENDER)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Slider(models.Model):
    alttext1=models.CharField(max_length=100,null=True)
    alttext2=models.CharField(max_length=100,null=True)
    alttext3=models.CharField(max_length=100,null=True)
    sliderimg=models.ImageField(upload_to="static/img/")
    status=models.BooleanField(default=True)

class Overview(models.Model):
    product=models.ForeignKey(Product,related_name='overview',on_delete=models.CASCADE,null=True)
    author=models.ForeignKey(Merchant,on_delete=models.CASCADE,null=True)
    facts=models.TextField(null=True)
    travelinfo=models.TextField(null=True)
    status=models.BooleanField(default=True)

class Itnerary(models.Model):
    product=models.ForeignKey(Product,related_name='itner',on_delete=models.CASCADE,null=True)
    author=models.ForeignKey(Merchant,on_delete=models.CASCADE,null=True)
    day=models.CharField(max_length=250,default='Day 1',null=True)
    detail=models.TextField(null=True)
    status=models.BooleanField(default=True)

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


class ImageCollection(models.Model):
    product=models.ForeignKey(Product,related_name='img',on_delete=models.CASCADE,null=True)
    author=models.ForeignKey(Merchant,on_delete=models.CASCADE,null=True)
    image1=models.ImageField(upload_to='media')
    image2=models.ImageField(upload_to='media')
    image3=models.ImageField(upload_to='media')
    image4=models.ImageField(upload_to='media')
    

