from django.contrib import admin
from .models import *



# Сертификация
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'published')
    list_display_links = ('name',)  # Поле name будет нажимаемым и ссылаться на страницу редактирования объекта
    list_editable = ('published',)  # Поле published можно редактировать прямо в списке объектов
    list_filter = ('published',)  # Фильтр по кнопке
    search_fields = ('name',)  # Поиск по тексту и кнопке

admin.site.register(Certificate, CertificateAdmin)








# Членство
admin.site.register(Partnership)










# Субсидии
class LawInline(admin.TabularInline):
    model = Law
    extra = 2


class SubsidiesAdmin(admin.ModelAdmin):
    inlines = [LawInline]


admin.site.register(Subsidies, SubsidiesAdmin)











# 
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'date', 'published')
    list_display_links = ('name',)
    list_filter = ('date',)
    search_fields = ('name',)

admin.site.register(Exhibition, ExhibitionAdmin)