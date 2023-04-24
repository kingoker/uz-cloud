from django import forms
from django.contrib.auth.models import User
from .models import *


# Форма добавления Папки
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
        

# Форма добавления Файла
class addFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']
        widgets = {
            'file': forms.TextInput(attrs={'type':'File', 'class': 'popup__input', 'placeholder': 'Файл', 'required': True})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].label = ''