from django.contrib import admin

# Register your models here.

from .models import Accessories, Catalog, Color, Customer, EyeDoctor, Lenses, OrderList, Orderr, Prescription, Rim, ShopEmployee, Status


admin.site.register(Accessories)
admin.site.register(Catalog)
admin.site.register(Color)
admin.site.register(Customer)
admin.site.register(EyeDoctor)
admin.site.register(Lenses)
admin.site.register(OrderList)
admin.site.register(Orderr)
admin.site.register(Prescription)
admin.site.register(Rim)
admin.site.register(ShopEmployee)
admin.site.register(Status)

