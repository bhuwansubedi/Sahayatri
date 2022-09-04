from cgi import print_form
from ctypes import create_string_buffer
import imp
import json
from pickle import NONE
from urllib import request
from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import AddCategoryForm1, CreateUserForm,AddPackageForm
from django.contrib import messages
from sahayatriapp.models import BudgetCategory, Company,Slider,TypeCategory
from sahayatriapp.models import Product
from django.core import serializers

# Create your views here.
def index(request):
    query = Product.objects.all()
    cmp=Company.objects.all()
    sld=Slider.objects.all()
    context={'query':query,'cmp':cmp,'sld':sld}
    return render(request,'index.html',context)


#registration for normal user.
def registerUserPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            finalform = NONE
            if form.is_valid():
                finalform = form.save(commit=False)
                finalform.type_of_user = 'Customer'
                finalform.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'registerUser.html', context)


#registration for merchant.
def registerMerchantPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            finalform = NONE
            if form.is_valid():
                finalform = form.save(commit=False)
                finalform.type_of_user = 'Merchant'
                finalform.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'registerMerchant.html', context)


#login for both user and merchant.
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)


def prod_detail(request,pk):
    produc = Product.objects.get(id=pk)
    cmp=Company.objects.all()
    context = { 'produc':produc,'cmp':cmp}
    return render(request,'prod_detail.html',context)


def logoutUser(request):
	logout(request)
	return redirect('index')

def dashboard(request):
    return render(request,'admin.html')
    

def addPackage(request):
    if request.user.is_authenticated:
        catlist=BudgetCategory.objects.filter(status=True)
        data=TypeCategory.objects.filter(status=True)
        cmp=Company.objects.all()
        context = { 'cmp':cmp,'catlist':catlist,'data':data}
        return render(request,'addPackages.html',context)
             
    else:
        return redirect('/login')

def payment(request):
    return render(request,'payment.html')

def category1(request):
    return render(request,'category1.html')

def category2(request):
    return render(request,'category2.html')


def insertcategory(request):    
    if request.method=='POST':   
        id=request.POST['id']   
        name=request.POST['catname']
        startPrice=request.POST['startprice']
        endPrice=request.POST['endprice']
        status=request.POST['status'] 
        if id==0 or id == '':
            BudgetCategory.objects.create(name=name,startPrice=startPrice,endPrice=endPrice,status=status) 
            mess=1          
        else:
            BudgetCategory.objects.filter(id=id).update(name=name,startPrice=startPrice,endPrice=endPrice,status=status) 
            mess=2                             
        return JsonResponse({'mess':mess})
    return redirect('category1')


def GetBudgetCategoryList(request):
    catlist=BudgetCategory.objects.filter(status=True)
    #data=serializers.serialize('json',catlist)
    return JsonResponse({'catlist': list(catlist.values())})


def GetDetail(request):
    if request.method=='POST':
        catid=request.POST['catid']
        deta=BudgetCategory.objects.filter(id=catid)        
        det = serializers.serialize('json', deta)
        return HttpResponse(det, content_type="text/json-comment-filtered")       
        #return JsonResponse(deta)



#Category Type Views.... 

def AddTypeCategory(request):
    if request.method=='POST':   
        id=request.POST['id']   
        name=request.POST['typeName']
        status=request.POST['status'] 
        if id==0 or id == '':
            TypeCategory.objects.create(name=name,status=status) 
            mess=1          
        else:
            TypeCategory.objects.filter(id=id).update(name=name,status=status) 
            mess=2                             
        return JsonResponse({'mess':mess})
    return render(request,'TypeCategory.html')

def GetCategoryType(request):
    data=TypeCategory.objects.filter(status=True)
    return JsonResponse({'data': list(data.values())})

def GetCategoryTypeDetail(request):
    if request.method=='POST':
        id=request.POST['id']
        data=TypeCategory.objects.filter(id=id)        
        toJson = serializers.serialize('json', data)
        return HttpResponse(toJson, content_type="text/json-comment-filtered") 

def DeleteCategoryType(request):
    if request.method=='POST':
        id=request.POST['id']
        data = TypeCategory.objects.filter(id=id).delete()      
        return JsonResponse({'data':data})
