from django.shortcuts import render
from .models import *


def phoneNumbers(request):
    departments = Department.objects.all()

    context = {
        'departments': departments,
    }

    return render(request, 'phoneNumbers.html', context)
