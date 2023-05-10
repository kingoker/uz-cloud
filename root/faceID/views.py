from django.shortcuts import render
from hikvisionapi import Client


def faceID(request):
    client = Client('http://192.168.1.40', 'admin', 'dima1754422')
    users = client.faces.get_users()

    context = {
        'users': users,
    }

    return render(request, 'faceID.html', context)
