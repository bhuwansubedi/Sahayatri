from dataclasses import asdict
from distutils.command.upload import upload
from pyexpat import model
from re import T
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
    price =models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

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

    def __str__(self):
        return self.name

