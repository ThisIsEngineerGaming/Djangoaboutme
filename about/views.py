from django.shortcuts import render


def home(request):
    return render(request, 'about/home.html')


def me_biography(request):
    return render(request, 'about/me_biography.html')


def me_facts(request):
    return render(request, 'about/me_facts.html')


def city_info(request):
    return render(request, 'about/city_info.html')


def city_places(request):
    return render(request, 'about/city_places.html')
