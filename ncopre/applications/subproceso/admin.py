from django.contrib import admin

# Register your models here.
from .models import Field, SubProcess, FieldsSubProcess

admin.site.register(Field)
admin.site.register(SubProcess)
admin.site.register(FieldsSubProcess)
