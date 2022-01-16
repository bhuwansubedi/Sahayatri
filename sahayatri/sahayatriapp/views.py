from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')