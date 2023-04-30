from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from .views import *


urlpatterns = [
    path('', index, name='main'),
    path('folders/<int:folder_id>/', folder_view, name='folder_view'),
    path('delete-element/', delete_element, name='delete-element'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)