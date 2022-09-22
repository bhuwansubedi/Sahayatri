from django.contrib import admin
from django.urls import path,include
from sahayatriapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index, name='index'),
   path('registerUser/', views.registerUserPage, name="registerUser"),
   path('registerMerchant/', views.registerMerchantPage, name="registerMerchant"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
   
   path('addPackage', views.addPackage, name="addPackage"),     
   path('prod_detail/<str:pk>/', views.prod_detail, name="prod_detail"),
   path('filter/<str:pk>/', views.filter, name="filter"),
   path('search', views.search, name="search"),
   path('addtocart', views.addtocart, name="addtocart"),
   path('viewcart', views.viewcart, name="viewcart"),
   path('getPackageDetails/',views.getPackageDetails,name='getPackageDetails'),
   
   path('dashboard',views.dashboard,name='dashboard'),
   
   path('payment',views.payment,name='payment'),
   
   path('category1',views.category1,name='category1'),
   path('category2',views.category2,name='category2'),
   path('insertcategory/',views.insertcategory,name='insertcategory'),
   path('getBudgetList/',views.GetBudgetCategoryList,name='getBudgetList'),
   path('GetDetail/',views.GetDetail,name='GetDetail'),
   path('DistrictList/',views.getdistrict,name='DistrictList'),
   path('MuniList/',views.getmuni,name='MuniList'),
   path('InsertPackage/',views.InsertPackage,name='InsertPackage'),
   path('saveRating/',views.saveRating,name='saveRating'),
   path('profile/',views.profile,name='profile'),

   
   #Category Type CRUD URLS..
   path('typecategory/',views.AddTypeCategory,name='typecategory'),
   path('getcategorytype/',views.GetCategoryType,name='getcategorytype'),
   path('categorytypedetail/',views.GetCategoryTypeDetail,name='categorytypedetail'),
   path('deletecategorytype/',views.DeleteCategoryType,name='deletecategorytype'),


   #Password Reset URLS...

   path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

   path('reset_password_sent/', 
      auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
      name="password_reset_done"),

   path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

   path('reset_password_complete/', 
      auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
      name="password_reset_complete"),
]