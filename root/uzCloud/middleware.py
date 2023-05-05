from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve
from django.http import HttpRequest
from .models import *
from django.urls import reverse



class PageViewMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        resolved = resolve(request.path_info)
        view_name = resolved.view_name
        if view_name != 'django.views.static.serve' and not request.path_info.startswith(reverse('admin:index')):  # Exclude static files and admin pages
            # Get or create a PageView object for the current page
            page_view, _ = PageView.objects.get_or_create(url=request.path_info)
            page_view.views += 1
            page_view.save()
        return None
