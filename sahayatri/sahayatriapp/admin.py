from django.contrib import admin
from sahayatriapp.models import Company,Merchant,Product,Customer

# Register your models here.
admin.site.register(Company)
admin.site.register(Merchant)
admin.site.register(Product)
admin.site.register(Customer)