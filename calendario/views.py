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
        if result == None:
            return redirect('new_booking')
        else:

            total_date = Booking.objects.filter(date__year=year, date__month=month, date__day=day).values('date')
            date_1= total_date[:1]
            date_2=date_1[0]
            date = date_2["date"]
            all_booking_of_day = Booking.objects.filter(date__year=year, date__month=month, date__day=day).order_by('time')
            a=all_booking_of_day[0]




            return render(request, 'calendario/day.html', {'result': result,'date': date ,'time_booking': all_booking_of_day,'a': a})



def new_booking(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'calendario/new_booking.html', {'form': form})

def get_month_bookings(request):
    if request.is_ajax():
        month = request.GET['month']
        year = request.GET['year']

        result = Booking.objects.filter(date__year=year, date__month=month).values('date').annotate(
            number_of_bookings=Sum('pax'))

        response = {}
        for item in list(result):
            response[item['date'].strftime('%m-%d-%Y')] = item['number_of_bookings']

        return HttpResponse(json.dumps(response))
