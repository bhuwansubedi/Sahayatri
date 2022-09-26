from django.contrib import admin
from sahayatriapp.models import Bucketlist, Company, District,Merchant, Municipality, Order,Province,Product,Customer, Rating,Slider,BudgetCategory,TypeCategory

# Register your models here.
admin.site.register(Company)
admin.site.register(Merchant)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Slider)
admin.site.register(BudgetCategory)
admin.site.register(TypeCategory)
admin.site.register(Province)
admin.site.register(District)
admin.site.register(Municipality)
admin.site.register(Rating)
admin.site.register(Bucketlist)
admin.site.register(Order)
