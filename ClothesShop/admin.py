from django.contrib import admin
from .models import Shoe, Shirt, Seller, Sell


""" class CurseAdmin(admin.ModelAdmin):
  list_display = ['name', 'category']
  search_fields = ['name', 'category']
  list_filter = ['name']
 """
# Register your models here.
admin.site.register(Shoe)
admin.site.register(Shirt)
admin.site.register(Seller)
admin.site.register(Sell)