from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from sahayatriapp.models import Company

# Create your views here.
def index(request):
    cmp=Company.objects.all()
    context={'cmp':cmp}
    return render(request,'index.html',context)