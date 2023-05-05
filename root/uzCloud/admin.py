from django.contrib import admin
from .models import *


class PageViewAdmin(admin.ModelAdmin):
    list_display = ('url', 'views')


admin.site.register(File)
admin.site.register(Folder)
admin.site.register(PageView, PageViewAdmin)
