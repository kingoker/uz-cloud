from django.shortcuts import render
from .models import *


# Отображение главной страницы
def index(request):
    folders = Folder.objects.filter(parent_folder=None)
    files = File.objects.filter(folder=None)

    current_path = request.path_info
    segments = current_path.split('/')
    crumbs = []
    for i, segment in enumerate(segments):
        crumb = {'url': '/'.join(segments[:i+1]), 'name': segment}
        crumbs.append(crumb)

    context = {
        'folders': folders,
        'files': files,
        'crumbs': crumbs,
    }

    return render(request, 'index.html', context)