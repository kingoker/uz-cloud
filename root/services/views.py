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
    partnership = Partnership.objects.filter(published=True).last()

    context = {
        'partnership': partnership,
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
    subsidies = Subsidies.objects.filter(published=True)

    context = {
        'subsidies': subsidies,
    }

    return render(request, 'services/subsidies/subsidies.html', context)


# Страница субсидий-список
def subsidiesAbout(request, pk):
    subsidies = get_object_or_404(Subsidies, pk=pk)
    laws = Law.objects.filter(subsidy=subsidies)

    context = {
        'subsidies': subsidies,
        'laws': laws,
    }

    return render(request, 'services/subsidies/listSubsidies.html', context)


# Страница субсидий-форма
def subsidiesForm(request):

    context = {

    }

    return render(request, 'services/subsidies/form.html', context)















# **********************************#
# Страница Выставок
def exhibitions(request):
    exhibitions = Exhibition.objects.filter(published=True).order_by('date')

    context = {
        'exhibitions': exhibitions,
    }

    return render(request, 'services/exhibitions/exhibitions.html', context)



# Страница Сертификатов-список
def exhibitionsAbout(request, pk):
    exhibitions = get_object_or_404(Exhibition, pk=pk)

    context = {
        'exhibitions': exhibitions,
    }

    return render(request, 'services/exhibitions/about.html', context)


# Страница Сертификатов
def exhibitionsForm(request):

    context = {

    }

    return render(request, 'services/exhibitions/form.html', context)