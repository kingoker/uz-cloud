from django.shortcuts import render


def phoneNumbers(request):
    return render(request, 'phoneNumbers.html')
