from django.shortcuts import render
from datetime import date
from .models import *


def phoneNumbers(request):
    departments = Department.objects.all()
    structure = Structure.objects.latest('upload_date')

    context = {
        'departments': departments,
        'structure': structure,
    }

    return render(request, 'phoneNumbers.html', context)
