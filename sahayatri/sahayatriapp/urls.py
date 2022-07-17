from django.contrib import admin
from django.urls import path,include
from sahayatriapp import views

urlpatterns = [
   path('', views.index, name='index'),
   path('registerUser/', views.registerUserPage, name="registerUser"),
   path('registerMerchant/', views.registerMerchantPage, name="registerMerchant"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
   path('addPackage/', views.addPackage, name="addPackage"),     
   path('prod_detail/<str:pk>/', views.prod_detail, name="prod_detail"),
   path('dashboard',views.dashboard,name='dashboard'),
   path('payment',views.payment,name='payment'),
   path('category1',views.category1,name='category1'),
   path('category2',views.category2,name='category2'),
   path('insertcategory/',views.insertcategory,name='insertcategory'),
   path('getBudgetList/',views.GetBudgetCategoryList,name='getBudgetList'),
   path('GetDetail/',views.GetDetail,name='GetDetail'),
]