from django.shortcuts import redirect, render
from .models import *
from .forms import *


# Отображение главной страницы
def index(request):
    folders = Folder.objects.filter(parent_folder=None)
    files = File.objects.filter(folder=None)
    folder = None

    # Форма добавления папки
    folderForm = addFolderForm()
    add_folder(request, folder)

    # Форма добавления файла
    fileForm = addFileForm()
    add_file(request, folder)

    context = {
        'fileForm': fileForm,
        'folder': folder,
        'folders': folders,
        'files': files,
        'folderForm': folderForm,
    }

    return render(request, 'index.html', context)


# Отображение содержимого папки
def folder_view(request, folder_id):
    folder = Folder.objects.get(pk=folder_id)
    subfolders = Folder.objects.filter(parent_folder=folder)
    files = File.objects.filter(folder=folder)

    # Форма добавления папки
    folderForm = addFolderForm()
    add_folder(request, folder)

    # Форма добавления файла
    fileForm = addFileForm()
    add_file(request, folder)

    context = {
        'fileForm': fileForm,
        'folderForm': folderForm,
        'folder': folder,
        'subfolders': subfolders,
        'files': files,
    }

    return render(request, 'index.html', context)




# Функция обработки формы добавления папки
def add_folder(request, folder):
    if request.method == 'POST':
        folder_form = addFolderForm(request.POST)
        if folder_form.is_valid():
            newfolder = folder_form.save(commit=False)
            newfolder.author = request.user
            newfolder.parent_folder = folder
            newfolder.save()


# Добавление файлов
def add_file(request, folder):
    if request.method == 'POST':
        file_form = addFileForm(request.POST, request.FILES)
        if file_form.is_valid():
            newfile = file_form.save(commit=False)
            newfile.author = request.user
            newfile.folder = folder
            newfile.save()
            print('Файл сохранён')
        else:
            print('Форма не валидна')
