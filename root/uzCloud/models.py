import os
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Метод для определения пути загрузки файла
def file_upload_to(instance, filename):
    folder_name = instance.folder.name if instance.folder else 'root_file'
    return f'files/{folder_name}/{filename}'





# Модель файлов
class File(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True,)
    file = models.FileField(upload_to=file_upload_to)
    folder = models.ForeignKey('Folder', on_delete=models.CASCADE, null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

# Задаём имя файла
@receiver(post_save, sender=File)
def update_folder_name(sender, instance, **kwargs):
    if instance.file and not instance.name:  # проверяем, что имя файла не заполнено и файл загружен
        file_name = os.path.basename(instance.file.name)  # извлекаем имя загруженного файла
        instance.name = file_name  # устанавливаем имя файла равным имени загруженного файла
        instance.save()  # сохраняем изменения в модели File




# Модель Папок
class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Папка'
        verbose_name_plural = 'Папки'
