from django.shortcuts import render


def index(request):
    return render(request, 'portal/index.html')


def flights(request):
    return render(request, 'portal/index.html')
