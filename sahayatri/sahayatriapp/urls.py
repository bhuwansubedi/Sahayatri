from django.contrib import admin
from django.urls import path,include
from sahayatriapp import views

urlpatterns = [
   path('', views.index, name='index'),
   path('registerUser/', views.registerUserPage, name="registerUser"),
   path('registerMerchant/', views.registerMerchantPage, name="registerMerchant"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),   

]