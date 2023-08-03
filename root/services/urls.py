from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *


urlpatterns = [
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),


    path('', services, name='services'),



    # Сертификация
    path('sertificats/', sertificats, name='sertificats'),
    path('sertificatsAbout/<int:pk>/', sertificatsAbout, name='sertificatsAbout'),
    path('sertificatsForm/', sertificatsForm, name='sertificatsForm'),


    # Членство
    path('partnership/', partnership, name='partnership'),
    path('partnershipForm/', partnershipForm, name='partnershipForm'),


    # Субсидии
    path('subsidies/', subsidies, name='subsidies'),
    path('subsidiesAbout/', subsidiesAbout, name='subsidiesAbout'),
    path('subsidiesForm/', subsidiesForm, name='subsidiesForm'),


    # Выставки
    path('exhibitions/', exhibitions, name='exhibitions'),
    path('exhibitionsAbout/', exhibitionsAbout, name='exhibitionsAbout'),
    path('exhibitionsForm/', exhibitionsForm, name='exhibitionsForm'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)