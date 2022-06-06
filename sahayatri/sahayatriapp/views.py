from ctypes import create_string_buffer
from pickle import NONE
from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from sahayatriapp.models import Company
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def index(request):
    cmp=Company.objects.all()
    context={'cmp':cmp}
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



def logoutUser(request):
	logout(request)
	return redirect('index')