from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phoneNumbers/', include('phoneNumbers.urls'), name='phoneNumbers'),
    path('', include('uzCloud.urls')),
]
