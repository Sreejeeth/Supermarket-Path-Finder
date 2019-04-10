    
from django.contrib import admin

# Register your models here.

from supermarket.models import Productdb,Category,About

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','category','image','price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available','image', 'created', 'updated',]
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Productdb, ProductAdmin)

admin.site.register(About)