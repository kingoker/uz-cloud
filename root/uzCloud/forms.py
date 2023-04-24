from django import forms
from django.contrib.auth.models import User
from .models import *


# Форма добавления Папки
class addFolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
        

# Форма добавления Файла
class addFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']