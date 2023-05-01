from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import *
from .forms import *

def creating(request):
    return render(request, 'creating.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


# Отображение главной страницы
@login_required
def index(request):
    folders = Folder.objects.filter(parent_folder=None)
    files = File.objects.filter(folder=None)
    folder = None

    # Создание новой папки
    if request.method == 'POST':
        folderForm = addFolderForm(request.POST)
        if folderForm.is_valid():
            folder = folderForm.save(request.user, folder)
            if folder.parent_folder_id == None:
                return redirect('main')
            else:
                return redirect('folder_view', folder_id=folder.parent_folder_id)
    else:
        folderForm = addFolderForm()


    # Форма добавления файла
    if request.method == 'POST':
        fileForm = addFileForm(request.POST, request.FILES)
        if fileForm.is_valid():
            file = fileForm.save(request.user, folder)
            if file.folder_id == None:
                return redirect('main')
            else:
                return redirect('folder_view', folder_id=file.folder_id)
    else:
        fileForm = addFileForm()


    context = {
        'fileForm': fileForm,
        'folder': folder,
        'folders': folders,
        'files': files,
        'folderForm': folderForm,
    }

    return render(request, 'hujjatlar.html', context)


# Отображение содержимого папки
@login_required
def folder_view(request, folder_id):
    folder = Folder.objects.get(pk=folder_id)
    subfolders = Folder.objects.filter(parent_folder=folder)
    files = File.objects.filter(folder=folder)

    # Создание новой папки
    if request.method == 'POST':
        folderForm = addFolderForm(request.POST)
        if folderForm.is_valid():
            folder = folderForm.save(request.user, folder)
            print('Your code')
            print(folder.__dict__)
            if folder.parent_folder_id == None:
                return redirect('main')
            else:
                return redirect('folder_view', folder_id=folder.parent_folder_id)
    else:
        folderForm = addFolderForm()


    # Форма добавления файла
    if request.method == 'POST':
        fileForm = addFileForm(request.POST, request.FILES)
        if fileForm.is_valid():
            file = fileForm.save(request.user, folder)
            if file.folder_id == None:
                return redirect('main')
            else:
                return redirect('folder_view', folder_id=file.folder_id)
    else:
        fileForm = addFileForm()


    context = {
        'fileForm': fileForm,
        'folderForm': folderForm,
        'folder': folder,
        'subfolders': subfolders,
        'files': files,
    }

    return render(request, 'hujjatlar.html', context)



# Удаление файла или папки
@require_POST
def delete_element(request):
    element_id = request.POST.get('element_id')
    element_type = request.POST.get('element_type')
    if element_type == 'folder':
        folder = get_object_or_404(Folder, id=element_id)
        folder.delete()
    elif element_type == 'file':
        file = get_object_or_404(File, id=element_id)
        file.delete()
    return JsonResponse({'success': True})