from django import forms
from django.contrib.auth.models import User
from .models import *


# Форма добавления папки
class addFolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'popup__input', 'placeholder': 'Название папки', 'required': True})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ''

    def save(self, author, parent_folder):
        folder = super().save(commit=False)
        folder.author = author
        folder.parent_folder = parent_folder
        folder.save()
        return folder
        


# Форма добавления Файла
class addFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'popup__input', 'required': True})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].label = ''
    
    def save(self, user, folder):
        file = super().save(commit=False)
        file.author = user
        file.folder = folder
        file.save()
        return file
