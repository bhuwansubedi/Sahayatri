from distutils.command.upload import upload
from pyexpat import model
from unicodedata import name
from django.db import models

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