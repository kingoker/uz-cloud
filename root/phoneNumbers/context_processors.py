from datetime import date
from .models import *


def users_with_birthday(request):
    today = date.today()
    users_with_birthday = CustomUser.objects.filter(birth_date__day=today.day, birth_date__month=today.month)[:1]
    return {'users_with_birthday': users_with_birthday}