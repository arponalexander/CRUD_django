from django.contrib import admin
from .models import Company_B00, Insurance_B00, Insurance_B01
from django.db import models


class CRUDAdminLook(admin.ModelAdmin):
    list_display = ['Company_Rec']


admin.site.register(Company_B00, CRUDAdminLook)
admin.site.register(Insurance_B00)
admin.site.register(Insurance_B01)
