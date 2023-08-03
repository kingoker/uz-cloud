from django.contrib import admin
from .models import *


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'published')
    list_display_links = ('name',)  # Поле name будет нажимаемым и ссылаться на страницу редактирования объекта
    list_editable = ('published',)  # Поле published можно редактировать прямо в списке объектов
    list_filter = ('published',)  # Фильтр по кнопке
    search_fields = ('name',)  # Поиск по тексту и кнопке

admin.site.register(Certificate, CertificateAdmin)
