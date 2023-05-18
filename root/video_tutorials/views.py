from django.shortcuts import render, get_object_or_404
from .models import *


def videoList(request):
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'videoList.html', context)



def course_lessons(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lesson_set.all()
    context = {
        'course': course,
        'lessons': lessons,
    }
    return render(request, 'course_lessons.html', context)
