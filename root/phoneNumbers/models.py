from django.db import models



class Position(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class CustomUser(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    internal_number = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='userPhotos/', blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


# Структура
class Structure(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='structure/')

    class Meta:
        verbose_name = 'Структура'
        verbose_name_plural = 'Структуры'
