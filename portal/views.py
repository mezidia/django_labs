from django.shortcuts import render
from .models import Flight


def index(request):
    return render(request, 'portal/index.html')


def about(request):
    return render(request, 'portal/about.html')


def contacts(request):
    return render(request, 'portal/contacts.html')


def flights(request):
    flights_data = Flight.objects.all().order_by('-flight_created')
    context = {'flights': flights_data}
    return render(request, 'portal/flights.html', context)


def flight(request, id):
    flight_object = Flight.objects.get(pk=id)
    context = {'flight': flight_object}
    return render(request, 'portal/flight.html', context)

