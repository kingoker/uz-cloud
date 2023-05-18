from django.contrib import admin
from .models import *


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 2


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]


admin.site.register(Course, CourseAdmin)