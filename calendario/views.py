import json
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from .models import Event


def index(request):
    return render(request, 'calendario/month.html')


def get_month_events(request):
    if request.is_ajax():
        month = request.GET['month']
        year = request.GET['year']

        result = Event.objects.filter(date__year=year, date__month=month).values('date').annotate(
            number_of_events=Count('date'))

        response = {}
        for item in list(result):
            response[item['date'].strftime('%m-%d-%Y')] = item['number_of_events']

        return HttpResponse(json.dumps(response))


def get_day_events(request):
    return render(request, 'calendario/day.html')
