from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    pass
class UserAdmin(admin.ModelAdmin):
    pass
class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product,ProductAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)