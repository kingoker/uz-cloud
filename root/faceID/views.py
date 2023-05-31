from django.shortcuts import render
from pyhik.hikvision import HikCamera


def faceID(request):
    camera = HikCamera('192.168.1.41', 'admin', 'dima1754422')
    reports = camera.get_event_triggers()
    
    context = {
        'reports': reports,
    }

    return render(request, 'faceID.html', context)
