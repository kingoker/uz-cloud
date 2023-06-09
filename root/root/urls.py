from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phoneNumbers.urls'), name='phoneNumbers'),
    path('uzCloud/', include('uzCloud.urls'), name='uzCloud'),
    path('video/', include('video_tutorials.urls'), name='videoList'),
]
