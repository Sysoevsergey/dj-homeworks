from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('1.2-requests-templates/pagination/data-398-2018-08-30.csv', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        stations_data = list(reader)
        paginator = Paginator(stations_data, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page,
            'page': page,
            }
    return render(request, 'stations/index.html', context)
