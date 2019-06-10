# Create your views here.
import csv

from django.utils import timezone
from django.http import HttpResponse

from .models import WeightClass, NasdaqIndex, NasdaqAverage, Country, Airport

import exoapp.src.nasdaq_reader as nasdaq_reader
#import exoapp.src.reader as reader


def index(request):
    return HttpResponse("Hello, world. You're at the exocute index.")

def import_nasdaq_index(request):
    response = "<h1>You're at the page for importing the nasdaq salmon index.</h1>"
    file_name = '/Users/ronny/PycharmProjects/exocute/data/salmonIndexHistory.csv'
    result = nasdaq_reader.salmon_index(file_name)
    list_class = result['list_class']
    list_average = result['list_average']

    response += '<p>Price (class) records imported: ' + str(len(list_class)) + ' records.</p>'
    response += '<p>Price (week average) records imported: ' + str(len(list_average)) + ' records.</p>'
    for item in list_class:
        new = NasdaqIndex(
            weight_class = WeightClass.objects.get(pk=item['weight_class']),
            week = item['week'],
            price=item['price'],
            distribution=item['distribution'],
            standard_deviation=item['standard_deviation'],
            created=timezone.now(),
            updated=timezone.now()
        )
        new.save()
        # KEEP AS ALTERNATIVE WAY (NOT TESTED IF PK/WEIGHT_CLASS WORKS
        #weight_class = WeightClass.objects.get(pk=item['weight_class'])
        #response += weight_class.weight_class
        #NasdaqIndex.objects.create(weight_class=weight_class, week=item['week'], price=item['price'], distribution=item['distribution'], standard_deviation=item['standard_deviation'], created=timezone.now(), updated=timezone.now())

    for item in list_average:
        new = NasdaqAverage(
            week = item['week'],
            price_average=item['price'],
            volume=item['volume'],
            created=timezone.now(),
            updated=timezone.now()
        )
        new.save()

    return HttpResponse(response)

def import_weight_classes(request):
    file_path = '/Users/ronny/PycharmProjects/exocute/data/exo_weightclasses.csv'

    # Test if records already exists
    items = WeightClass.objects.all()
    length = len(items)
    if length:
        output = str(length) + ' records already exists in the table. No new data is added to the database'
        return HttpResponse(status=201, content=output)
    else:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            i = 0
            for record in csv_reader:
                print(record, type(record))
                WeightClass.objects.create(weight_class=record[0], created=timezone.now(), updated=timezone.now())
                i +=1
        output = str(i) + ' records added to the database.'
        return HttpResponse(status=201, content=output)

def laboratory(request):
    response = "You're looking at the laboratory page."
    return HttpResponse(response)

def import_data(request):
    # file_path = request.GET.get('file_path') // from url
    # file_path = '/Users/ronny/PycharmProjects/exocute/data/exo_weightclasses.csv'
    # file_path = '/Users/ronny/PycharmProjects/exocute/data/iso_countries.csv'
    file_path = '/Users/ronny/PycharmProjects/exocute/data/airports.csv'
    action = True
    if action == True:
        delimiter = ';'
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=delimiter)

            for record in csv_reader:
                iso_country = Country.objects.get(pk=record[3])
                print(record)
                # WeightClass.objects.create(weight_class_text=record[0], created=timezone.now(), updated=timezone.now())
                # Country.objects.create(iso_country=record[1], country=record[0], created=timezone.now(), updated=timezone.now())
                Airport.objects.create(iata_code=record[0], name=record[1], type=record[2], iso_country=iso_country, iso_region=record[4], municipality=record[5], latitude_deg=record[7], longitude_deg=record[8], created=timezone.now(), updated=timezone.now())

        return HttpResponse(status=201, content='Records added to the database.')

    else:

        return HttpResponse(status=201, content='Functionality switched off—no data added to the database.')