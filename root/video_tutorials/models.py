from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course_images')
    lesson_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    url = models.URLField()
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
