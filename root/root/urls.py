from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('phoneNumbers.urls'), name='phoneNumbers'),
    path('uzCloud/', include('uzCloud.urls'), name='uzCloud'),
    path('faceid/', include('faceID.urls'), name='faceid'),
    path('video/', include('video_tutorials.urls'), name='videoList'),
    path('chatgpt/', include('chatgpt.urls'), name='chatgpt'),
]
