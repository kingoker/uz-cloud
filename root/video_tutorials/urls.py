from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *


urlpatterns = [
    path('', videoList, name='videoList'),
    path('courses/<int:course_id>/', course_lessons, name='courseLessons'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)