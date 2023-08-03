from django.shortcuts import get_object_or_404, render
from .models import *


# Главная страница
def services(request):

    context = {

    }

    return render(request, 'services/index.html', context)









# **********************************#
# Страница Сертификатов
def sertificats(request):
    # Получаем все опубликованные сертификаты из базы данных
    certificates = Certificate.objects.filter(published=True)

    context = {
        'certificates': certificates,  # Передаем опубликованные сертификаты в контекст шаблона
    }

    return render(request, 'services/sertification/sertificats.html', context)



# Страница Сертификатов-список
def sertificatsAbout(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)

    context = {
        'certificate': certificate,  # Передаем сертификат в контекст шаблона
    }

    return render(request, 'services/sertification/about.html', context)


# Страница Сертификатов
def sertificatsForm(request):

    context = {

    }

    return render(request, 'services/sertification/form.html', context)












# **********************************#
# Страница Членства
def partnership(request):

    context = {

    }

    return render(request, 'services/partnership/about.html', context)


# Страница Сертификатов-список
def partnershipForm(request):

    context = {

    }

    return render(request, 'services/sertification/form.html', context)














# **********************************#
# Страница Субсидий
def subsidies(request):

    context = {

    }

    return render(request, 'services/subsidies/subsidies.html', context)


# Страница Сертификатов-список
def subsidiesAbout(request):

    context = {

    }

    return render(request, 'services/subsidies/listSubsidies.html', context)


# Страница Сертификатов
def subsidiesForm(request):

    context = {

    }

    return render(request, 'services/subsidies/form.html', context)















# **********************************#
# Страница Выставок
def exhibitions(request):

    context = {

    }

    return render(request, 'services/exhibitions/exhibitions.html', context)


# Страница Сертификатов-список
def exhibitionsAbout(request):

    context = {

    }

    return render(request, 'services/exhibitions/about.html', context)


# Страница Сертификатов
def exhibitionsForm(request):

    context = {

    }

    return render(request, 'services/exhibitions/form.html', context)