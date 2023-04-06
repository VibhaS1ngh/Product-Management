from django.contrib import admin
from.models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ['name','mobile','email','password']
admin.site.register(User,UserAdmin)




class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','brand','price','quantity','description']

admin.site.register(Product,ProductAdmin)