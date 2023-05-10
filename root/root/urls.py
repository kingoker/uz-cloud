from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phoneNumbers.urls'), name='phoneNumbers'),
    path('faceid/', include('faceID.urls'), name='faceid'),
    path('uzCloud/', include('uzCloud.urls'), name='uzCloud'),
]
