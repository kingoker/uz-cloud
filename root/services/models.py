from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


# Сертификация
class Certificate(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = CKEditor5Field('Text', config_name='extends')
    image = models.FileField(upload_to='services/certificates/', verbose_name='Изображение')  # Поле для загрузки файла
    text=CKEditor5Field('Text', config_name='extends')
    published = models.BooleanField(default=True, verbose_name='Опубликован')


    def __str__(self):
        return self.text[:50]  # Возвращает первые 50 символов текста сертификата (можно изменить)

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'