from django.contrib import admin
from django.urls import path,include
from sahayatriapp import views

urlpatterns = [
   path('', views.index, name='index'),
   path('registerUser/', views.registerUserPage, name="registerUser"),
   path('registerMerchant/', views.registerMerchantPage, name="registerMerchant"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
   
   path('addPackage', views.addPackage, name="addPackage"),     
   path('prod_detail/<str:pk>/', views.prod_detail, name="prod_detail"),
   path('filter/<str:pk>/', views.filter, name="filter"),
   path('booking_list', views.booking_list, name="booking_list"),
   path('getbookingdetail', views.getbookingdetail, name="getbookingdetail"),
   path('search', views.search, name="search"),
   path('addtocart', views.addtocart, name="addtocart"),
   path('viewcart', views.viewcart, name="viewcart"),
   path('merchant', views.merchant, name="merchant"),
   path('export_excel', views.export_excel, name="export_excel"),
   path('export_excel_package', views.export_excel_package, name="export_excel_package"),
   path('merchprofile', views.merchprofile, name="merchprofile"),
   path('createmerchprofile',views.createmerchprofile,name='createmerchprofile'),
   
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
]