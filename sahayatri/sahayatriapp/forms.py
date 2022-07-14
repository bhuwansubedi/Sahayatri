from dataclasses import fields
from logging import PlaceHolder
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer,Merchant,Product,BudgetCategory,TypeCategory
from django import forms

from sahayatriapp.models import Customer, Merchant


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CreateMerchantForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class AddPackageForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','image','category','description']
        labels = {
			'name': '',
		    'price': '',
		    'image': '',
		    'category': '',
		    'description': '',

		}
        widgets = {
	    	'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Package Name..','style':'width: 50%; border-color: #19cdd0;'}),
		    'price': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Package Price','style':'width: 50%; border-color: #19cdd0;'}),
		    'image': forms.FileInput(attrs={'class':'form-control','placeholder':'Upload Image','style':'width: 50%; border-color: #19cdd0;'}),
		    'category': forms.TextInput(attrs={'class':'form-control','placeholder':'Choose Category','style':'width: 50%; border-color: #19cdd0;'}),
		    'description': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Description','style':'width: 50%; border-color: #19cdd0;'}),
	    }

class AddCategoryForm1(ModelForm):
	class Meta:
		model=BudgetCategory
		fields=['name','startPrice','endPrice','status']
