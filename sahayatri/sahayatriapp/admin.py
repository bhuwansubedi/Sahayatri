from django.contrib import admin
from sahayatriapp.models import Company, District,Merchant, Municipality,Province,Product,Customer, Rating,Slider,BudgetCategory,TypeCategory,Order

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
admin.site.register(Order)
