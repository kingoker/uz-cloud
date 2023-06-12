from django.contrib import admin
from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'internal_number', 'phone_number')
    search_fields = ('full_name',)
    list_filter = ('position', 'birth_date')


admin.site.register(Department)
admin.site.register(Position)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Structure)