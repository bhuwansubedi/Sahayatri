from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from sahayatriapp.models import Company,Slider

# Create your views here.
def index(request):
    cmp=Company.objects.all()
    sld=Slider.objects.all()
    context={'cmp':cmp,'sld':sld}
    return render(request,'index.html',context)