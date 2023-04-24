from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *


urlpatterns = [
    path('', index, name='main'),
    path('folders/<int:folder_id>/', folder_view, name='folder_view'),
    path('delete-folder/', delete_folder, name='delete_folder'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)