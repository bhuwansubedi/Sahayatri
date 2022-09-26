
from cgi import print_form
from ctypes import create_string_buffer
import email
from email.mime import image
from fileinput import filename
from hashlib import new
import imp
from itertools import count, product
import json
from math import dist, prod
from multiprocessing import context
from pickle import NONE
from unicodedata import category, name
from urllib import request
from urllib.robotparser import RequestRate
from xmlrpc.client import DateTime
from django.db import models
from django.http.response import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from sahayatriapp.models import BudgetCategory, Bucketlist,Company, Merchant, Order,Rating,Slider,TypeCategory,Product,District,Municipality,Province,Customer
from sahayatriapp.models import Product
from django.core import serializers
from math import sqrt
import pandas as pd
import numpy as np
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import random
import warnings
from django.db.models import Avg,Sum

from django.template.loader import render_to_string
import csv
from django.contrib.auth.models import User
warnings.filterwarnings('ignore')
# Create your views here.
def standardize(row):
    new_row = (row - row.mean()) / (row.max() - row.min())
    return new_row 


def read_rating_cs(request):
    prod=Product.objects.all()
    rating=Rating.objects.all()
    x=[]
    y=[]
    A=[]
    B=[]
    C=[]
    D=[]
    for item in prod:
        x=[item.id,item.name,item.price,item.image,item.days,item.nights,item.valid_date]
        y+=[x]
    prod_df=pd.DataFrame(y,columns=['prod_id','prod_name','prod_price','image','days','nights','valid_date'])
    for item in rating:
        A=[item.user.id,item.item.id,item.rating]
        B+=[A]
    rating_df=pd.DataFrame(B,columns=['user_id','prod_id','rating'])
    rating_df['user_id']=rating_df['user_id'].astype(str).astype(np.int64)
    rating_df['prod_id']=rating_df['prod_id'].astype(str).astype(np.int64)
    rating_df['rating']=rating_df['rating'].astype(str).astype(np.float)
    if request.user.is_authenticated:
        userid=request.user.id
        userInput=Rating.objects.select_related('item').filter(user=userid)
        if(userInput.count()==0):
            recommenderQuery=None
            userInput=None
        else:
            for item in userInput:
                C=[item.item.name,item.rating]
                D+=[C]
            inputPackage=pd.DataFrame(D,columns=['prod_name','rating'])
            #print("List of Rated packages by "+request.user.username)
            inputPackage['rating']=inputPackage['rating'].astype(str).astype(np.float)
            inputId=prod_df[prod_df['prod_name'].isin(inputPackage['prod_name'].tolist())]
            inputPackage=pd.merge(inputPackage,inputId)
            #print(inputPackage)

            userSubset=rating_df[rating_df['prod_id'].isin(inputPackage['prod_id'].tolist())]
            #print(userSubset)
            userSubsetGroup=userSubset.groupby('user_id')
            userSubsetGroup = sorted(userSubsetGroup,  key=lambda x: len(x[1]), reverse=True)
            #print(userSubsetGroup[0:])  
            userSubsetGroup = userSubsetGroup[0:]
            pearsonCorrelationDict = {}

            for name, group in userSubsetGroup:
                group=group.sort_values(by='prod_id')
                inputPackage=inputPackage.sort_values(by='prod_id')
                nRatings=len(group)

                temp_df=inputPackage[inputPackage['prod_id'].isin(group['prod_id'].tolist())]
                tempRatingList=temp_df['rating'].tolist()
                tempGroupList = group['rating'].tolist()
                Sxx = sum([i**2 for i in tempRatingList]) - pow(sum(tempRatingList),2)/float(nRatings)
                Syy = sum([i**2 for i in tempGroupList]) - pow(sum(tempGroupList),2)/float(nRatings)
                Sxy = sum( i*j for i, j in zip(tempRatingList, tempGroupList)) - sum(tempRatingList)*sum(tempGroupList)/float(nRatings)                
                if Sxx != 0 and Syy != 0:
                    pearsonCorrelationDict[name] = Sxy/sqrt(abs(Sxx*Syy))
                else:
                    pearsonCorrelationDict[name] = 0
            #print(pearsonCorrelationDict.items())

            pearsonDF = pd.DataFrame.from_dict(pearsonCorrelationDict, orient='index')
            pearsonDF.columns = ['similarityIndex']
            #print(pearsonDF)
            pearsonDF['user_id']=pearsonDF.index
            pearsonDF.index = range(len(pearsonDF))
            #print(pearsonDF.head())
            topUsers=pearsonDF.sort_values(by='similarityIndex', ascending=False)[0:]
            #print(topUsers.head())

            topUsersRating=topUsers.merge(rating_df, left_on='user_id', right_on='user_id', how='inner')
            topUsersRating.head()

            topUsersRating['weightedRating'] = topUsersRating['similarityIndex']*topUsersRating['rating']
            topUsersRating.head()

            tempTopUsersRating = topUsersRating.groupby('prod_id').sum()[['similarityIndex','weightedRating']]
            tempTopUsersRating.columns = ['sum_similarityIndex','sum_weightedRating']
            #print(tempTopUsersRating.head())

            recommendation_df = pd.DataFrame()
            #Now we take the weighted average
            recommendation_df['weighted average recommendation score'] = tempTopUsersRating['sum_weightedRating']/tempTopUsersRating['sum_similarityIndex']
            recommendation_df['prod_id'] = tempTopUsersRating.index
            recommendation_df.head()

            recommendation_df = recommendation_df.sort_values(by='weighted average recommendation score', ascending=False)
            recommender=prod_df.loc[prod_df['prod_id'].isin(recommendation_df.head(6)['prod_id'].tolist())]
            #print(recommender)
            return recommender.to_dict('records')        
    # rate_list = Rating.objects.all()    
    # rating = rate_list.values_list('id','item', 'user', 'rating')  
    # df = pd.DataFrame.from_records(rating,index=0)    
    # ptable=pd.pivot_table(df,values='0',index=['0','0'],columns=['0'])
    # print(ptable)
    # df.fillna(0)
    # ratings_std=df.apply(standardize)
    # user_similarity = cosine_similarity(ratings_std)
    # user_similarity_df = pd.DataFrame(user_similarity, index=df.index, columns=df.index) 
    # print (user_similarity_df)          
    # def get_similar_product(item,item_rate):
    #     mean_rating=2.5
    #     similar_score = user_similarity_df[item] * (item_rate - mean_rating) # 2.5 is the mean of the ratings
    #     similar_score = similar_score.sort_values(ascending=False)
    #     return similar_score[:10]
    # print(get_similar_product(36,5))
    # # num=userid 
    # # similar_users=get_similar_product(num,item_rate)    
    # # users = similar_users.index.values.tolist()
    # # print(users)
    # # new_ratings = df.rating[users, :]
    # # new_ratings = new_ratings.fillna(0)
    # # print(new_ratings)



def index(request):
    recommended= read_rating_cs(request)           
    generic_list=Product.objects.all()    
    cmp=Company.objects.all()
    sld=Slider.objects.all()
    cat=TypeCategory.objects.all()     
    if request.user.is_authenticated and request.user.is_staff and request.user.username!='superadmin':
        return redirect('merchant')
    elif request.user.is_authenticated and request.user.is_superuser :
        return redirect('admin:index')
    else: 
        count=0  
        if request.user.is_authenticated:
            count=Bucketlist.objects.filter(user=request.user).count()    
        category='All'
        context={'query':generic_list,'cmp':cmp,'sld':sld,'recomlist':recommended,'cat':cat,'category':category,'count':count}           
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

def merchant(request):    
    if request.user.is_authenticated and request.user.is_staff and request.user.username!='superadmin':  
        blist=Bucketlist.objects.filter(posted_by=request.user.id)             
        bcount=blist.count()        
        prodlist=Product.objects.filter(posted_by=request.user)                
        for p in prodlist:            
            tot=Rating.objects.filter(item=p).aggregate(Avg('rating'))  
            rtval=list(tot.values())            
            format_float = round(rtval[0],2)                 
            # p.avg_rating=("{0:.3f}".format(tot))
            # print(p.avg)
            # print(p.avg_rating)
            Product.objects.filter(id=p.id).update(avg_rating=format_float)
        prod_list=Product.objects.filter(posted_by=request.user)
        avrating=prod_list.aggregate(Avg('avg_rating'))
        rtaval=list(avrating.values())            
        avg_rating = round(rtaval[0],2)
       # print(prod_list.avg_rating)        
        prod_count=prod_list.count()   
        order_list=Order.objects.filter(user=request.user)
        order_count=order_list.count()        
        total_order_value=0
        for t in order_list:
            total_order_value=total_order_value + t.total                
        context={'blist':blist,'bcount':bcount,'prod_list':prod_list,'prod_count':prod_count,'order_list':order_list,
        'order_count':order_count,'tov':total_order_value,'avg_rating':avg_rating}
        return render(request,'admin.html',context)

def booking_list(request):
    if request.user.is_authenticated and request.user.is_staff and request.user.username!='superadmin':
        b_list=Bucketlist.objects.filter(posted_by=request.user.id)        
        context={'blist':b_list}
        return render(request,'bookinglist.html',context)

def export_excel(request):
    if request.user.is_authenticated and request.user.is_staff and request.user.username!='superadmin':
        b_list=Bucketlist.objects.filter(posted_by=request.user.id)                
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Booking List.csv"'        
        writer = csv.writer(response)
        writer.writerow(['Booking List'])       
        writer.writerow(['Name','Price','Booked By'])
        for b in b_list:
            writer.writerow([b.item.name,b.item.price,b.user.username])

    return response

def export_excel_package(request):
    if request.user.is_authenticated and request.user.is_staff and request.user.username!='superadmin':
        b_list=Product.objects.filter(posted_by=request.user)                
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Package_List.csv"'        
        writer = csv.writer(response)
        writer.writerow(['Package List'])       
        writer.writerow(['Name','Price','Duration','Valid Date'])
        for b in b_list:
            writer.writerow([b.name,b.price,str(b.days) +' Days '+ str(b.nights)+' Nights',b.valid_date])

    return response

def merchprofile(request):
    if request.user.is_authenticated and request.user.is_staff and request.user.username!='superadmin':
        if not Merchant.objects.filter(user=request.user).exists():
            context={}
        else:
            merch=Merchant.objects.filter(user=request.user)
            print(merch)
            context={'merch':merch}
        return render(request,'merchprofile.html',context)
def createmerchprofile(request):
    if request.user.is_authenticated and request.user.is_staff and request.user.username!='superadmin':
        if request.method=='POST':
            fullname=request.POST['cname']
            address=request.POST['caddres']
            pan=request.POST['pan']
            redgno=request.POST['redgno']
            email=request.POST['email']
            phone=request.POST['phone']
            if not Merchant.objects.filter(user=request.user).exists():               
                Merchant.objects.create(user=request.user,fullname=fullname,country=address,pan_no=pan,email=email,phone=phone,company_website=redgno)
                merch=Merchant.objects.filter(user=request.user)                
                return render(request,'merchprofile.html',{'merch':merch})
            else:
                Merchant.objects.filter(user=request.user).update(user=request.user,fullname=fullname,country=address,pan_no=pan,email=email,phone=phone,company_website=redgno)
                merch=Merchant.objects.filter(user=request.user)
                return render(request,'merchprofile.html',{'merch':merch})

def addtocart(request):
    if request.method=='POST':
        prodid=request.POST['id']
        action=request.POST['action']
        if action=='del':
            Bucketlist.objects.get(id=prodid).delete()
            return JsonResponse({'data':'suc'})        
        product=Product.objects.get(id=prodid)
        if not Bucketlist.objects.filter(user=request.user,item=product).exists():
            Bucketlist.objects.create(item=product,user=request.user,posted_by=product.posted_by.id) 
            count=Bucketlist.objects.filter(user=request.user).count()
            print(count)           
            return JsonResponse({'data':count})
        else:            
            return JsonResponse({'data':'fail'})


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

def search(request):
    recommended= read_rating_cs(request)           
    generic_list=Product.objects.all()    
    cmp=Company.objects.all()
    sld=Slider.objects.all()
    cat=TypeCategory.objects.all() 
    if request.method=='POST':
        key=request.POST['searchvalue']
        search_list=Product.objects.filter(name__contains=key)
        category='Search Results for '+key
        context={'query':search_list,'cmp':cmp,'sld':sld,'recomlist':recommended,'cat':cat,'category':category}
        return render(request,'index.html',context) 
    


def filter(request,pk):
    recommended= read_rating_cs(request)           
    generic_list=Product.objects.all()    
    cmp=Company.objects.all()
    sld=Slider.objects.all()
    cat=TypeCategory.objects.all()     
    if request.user.is_authenticated and request.user.is_staff and request.user.username!='superadmin':
        return redirect('addPackage')
    elif request.user.is_authenticated and request.user.is_superuser :
        return redirect('dashboard')
    else:                       
        if pk=='All':
            category='All'
            context={'query':generic_list,'cmp':cmp,'sld':sld,'recomlist':recommended,'cat':cat,'category':category}
            return render(request,'index.html',context)        
        else:
            catobj=TypeCategory.objects.get(id=pk)                       
            filter=Product.objects.filter(category=catobj)
            context={'query':filter,'cmp':cmp,'sld':sld,'recomlist':recommended,'cat':cat,'category':catobj.name}                 
            return render(request,'index.html',context)       

def logoutUser(request):
	logout(request)
	return redirect('index')

def dashboard(request):
    return render(request,'admin.html')

def viewcart(request):
    prov=Province.objects.all()
    munic=Municipality.objects.all()
    dist=District.objects.all() 
    cmp=Company.objects.all()
    sld=Slider.objects.all()
    count=Bucketlist.objects.filter(user=request.user).count() 
    total=Bucketlist.objects.filter(user=request.user)
    tot=0
    for t in total:
        tot=tot+int(t.item.price) 
    profile=0
    if Customer.objects.filter(user=request.user).exists():
        profile=Customer.objects.get(user=request.user)
    blist=Bucketlist.objects.filter(user=request.user)
    context={'cmp':cmp,'sld':sld,'prov':prov,'dist':dist,'muni':munic,'blist':blist,'profile':profile,'total':tot,'count':count}
    return render(request,'cart.html',context)
    

def addPackage(request):
    if request.user.is_authenticated and request.user.is_staff and request.user.username!='superadmin':
        catlist=BudgetCategory.objects.filter(status=True)
        data=TypeCategory.objects.filter(status=True)
        cmp=Company.objects.all()
        prov=Province.objects.all()
        context = { 'cmp':cmp,'catlist':catlist,'data':data,'prov':prov}
        return render(request,'addPackages.html',context)
    elif request.user.is_authenticated and request.user.is_superuser :
        return redirect('admin:index')
    elif request.user.is_authenticated:
        return redirect('index')             
    else:
        return redirect('/login')


def profile(request):
    cmp=Company.objects.all()
    sld=Slider.objects.all()
    prov=Province.objects.all()
    munic=Municipality.objects.all()
    dist=District.objects.all()    
    if Customer.objects.filter(user=request.user).exists():
        profile=Customer.objects.get(user=request.user)
    else:
        profile=0            
    #print(profile)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        gender=request.POST['gender']
        muni=request.POST['muni']
        province=request.POST['province']
        district=request.POST['district']
        country=request.POST['country']
        province=Province.objects.get(id=province)
        district=District.objects.get(id=district)
        muni=Municipality.objects.get(id=muni)
        if not Customer.objects.filter(user=request.user).exists():
            Customer.objects.create(user=request.user,fullname=name,email=email,phone=mobile,country=country,province=province,district=district,muni=muni,gender=gender)
            message="1"
            return JsonResponse({'data':message})
        else:
            Customer.objects.filter(user=request.user).update(user=request.user,fullname=name,email=email,phone=mobile,country=country,province=province,district=district,muni=muni,gender=gender)
            message="0"
            return JsonResponse({'data':message})
    context={'cmp':cmp,'sld':sld,'prov':prov,'dist':dist,'muni':munic,'profile':profile}
    return render(request,'profile.html',context)
def payment(request):
    if request.method=='POST':
        id=request.POST['id']
        total=request.POST['total']
        pay=request.POST['pay']  
        print(id,total,pay)      
        bl=Bucketlist.objects.get(id=id)
        prod=Product.objects.get(id=bl.item.id)
        if not Order.objects.filter(item=prod,user=request.user).exists():
            Order.objects.create(item=prod,user=request.user,payment=pay,total=total)
            if Order.objects.filter(item=prod,user=request.user).exists():
                Bucketlist.objects.filter(id=id).delete()            
                order=Order.objects.get(user=request.user)
                if pay=='esewa':
                    return render(request,'payment.html',{'order':order})
                else:
                    return redirect('index')



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
def InsertPackage(request):  
    if request.method=='POST':       
        action=request.POST['action']
        img1=request.FILES.get('img1')#['fileList']
        img2=request.FILES.get('img2')#['fileList']
        img3=request.FILES.get('img3')#['fileList']
        img4=request.FILES.get('img4')#['fileList']
        thumbImg=request.FILES.get('thumbImg')#['thumbImg']             
        pname=request.POST['pname']
        price=request.POST['price']
        desc=request.POST['desc']
        nights=request.POST['nights']
        days=request.POST['days']
        overview=request.POST['overview']
        packageType=request.POST['packageType']
        province=request.POST['province']
        district=request.POST['district']
        muni=request.POST['muni']
        catType=request.POST['catType']
        inclusions=request.POST['inclusions']
        exclusions=request.POST['exclusions']
        itner=request.POST['itner']
        vdate=request.POST['vdate']
        discount=request.POST['discount']
        author=request.user
        location=request.POST['location']        
        prov=Province.objects.get(id=province)
        dist=District.objects.get(id=district)
        muni=Municipality.objects.get(id=muni)
        cat=TypeCategory.objects.get(id=catType)
        bud=BudgetCategory.objects.get(id=packageType)
        if(action == '1'):
           Product.objects.create(name=pname,price=price,category=cat,budget=bud,image=thumbImg,description=desc,posted_by=author,inclusions=inclusions,exclusions=exclusions,Itnerary=itner,mapurl=location,days=days,nights=nights,province=prov,district=dist,muni=muni,valid_date=vdate,image1=img1,image2=img2,image3=img3,image4=img4,overview=overview)
           status='Success'       
           return JsonResponse({'status':status})
    return redirect('addPackage')
    

def GetBudgetCategoryList(request):
    catlist=BudgetCategory.objects.filter(status=True)
    #data=serializers.serialize('json',catlist)
    return JsonResponse({'catlist': list(catlist.values())})

def getbookingdetail(request):
    if request.method=='POST':
        bid=request.POST['bid']
        b_list=Bucketlist.objects.filter(id=bid)
        print(b_list)
        det = serializers.serialize('json', b_list)
        return HttpResponse(det, content_type="text/json-comment-filtered")

def GetDetail(request):
    if request.method=='POST':
        catid=request.POST['catid']
        deta=BudgetCategory.objects.filter(id=catid)        
        det = serializers.serialize('json', deta)
        return HttpResponse(det, content_type="text/json-comment-filtered")       
        #return JsonResponse(deta)

def saveRating(request):
    if request.method=='POST':
        prodid=request.POST['prodid']
        rating=request.POST['rating']
        user=request.user
        prod=Product.objects.get(id=prodid)
        if not Rating.objects.filter(item=prod,user=user).exists():
            Rating.objects.create(item=prod,user=user,rating=rating)
            return JsonResponse({'data':2})
        else:
            Rating.objects.filter(item=prod,user=user).update(item=prod,user=user,rating=rating) 
            return JsonResponse({'data':2})
        

def getdistrict(request):
    if request.method=='POST':
        provid=request.POST['pid']
        dist=District.objects.filter(province=provid)
        return JsonResponse({'dist':list(dist.values())}) 

def getmuni(request):
    if request.method=='POST':
        mid=request.POST['mid']
        muni=Municipality.objects.filter(district=mid)
        return JsonResponse({'muni':list(muni.values())}) 
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
