from django.shortcuts import render
from pyhik.hikvision import HikCamera


def faceID(request):
    camera = HikCamera('http://192.168.1.40', 'admin', 'dima1754422')
    users = camera.get_device_info()
    
    context = {
        'users': users,
    }

    return render(request, 'faceID.html', context)
