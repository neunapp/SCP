from django.contrib import admin

# Register your models here.

#local
from .models import BussinesUnit, Process

admin.site.register(BussinesUnit)
admin.site.register(Process)
