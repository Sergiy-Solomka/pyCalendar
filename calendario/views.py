import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count, Sum

from calendario.forms import PostForm
from .models import Booking


def index(request):
    return render(request, 'calendario/month.html')


def get_day_events(request):
    if not request.is_ajax():
        month = request.GET['month']
        year = request.GET['year']
        day = request.GET['day']

        total_pax = Booking.objects.filter(date__year=year, date__month=month, date__day=day).values('pax').aggregate(
            number_pax=Sum('pax'))
        result = total_pax["number_pax"]

        total_date = Booking.objects.filter(date__year=year, date__month=month, date__day=day).values('date')
        date_1= total_date[:1]
        date_2=date_1[0]
        date = date_2["date"]

        return render(request, 'calendario/day.html', {'result': result,'date': date})



def new_booking(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('dayevents')
    else:
        form = PostForm()
    return render(request, 'calendario/new_booking.html', {'form': form})

def get_month_bookings(request):
    if request.is_ajax():
        month = request.GET['month']
        year = request.GET['year']

        result = Booking.objects.filter(date__year=year, date__month=month).values('date').annotate(
            number_of_events=Count('date'))

        response = {}
        for item in list(result):
            response[item['date'].strftime('%m-%d-%Y')] = item['number_of_events']

        return HttpResponse(json.dumps(response))

def prueba(request):
    if not request.is_ajax():
        month = request.GET['month']
        year = request.GET['year']
        day = request.GET['day']

        result = Booking.objects.filter(date__year=year, date__month=month,date__day=day).values('pax').aggregate(number_pax=Sum('pax'))

        return render(request, 'calendario/prueba.html', {'result': result})