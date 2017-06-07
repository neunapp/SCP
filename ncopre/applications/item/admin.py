from django.contrib import admin

# Register your models here.

from .models import DetailProcess, Item, Voucher

admin.site.register(DetailProcess)
admin.site.register(Item)
admin.site.register(Voucher)
