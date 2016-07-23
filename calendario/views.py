import calendar
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Sum

from calendario.forms import PostForm
from .models import Booking
from django import forms

import datetime


def index(request):
    return render(request, 'calendario/month.html')


def get_day_events(request):
    month = request.GET['month']
    year = request.GET['year']
    day = request.GET['day']
    weekday = request.GET['weekday']

    # comprobamos que el dia no sea domingo o lunes
    if weekday == "0":
        return redirect('getsunday')
    if weekday == "1":
        return redirect('getmonday')

    start_time = datetime.datetime(100, 1, 1, 18, 00, 00)
    hours = [start_time.time()]

    for i in range(0, 16):
        start_time = start_time + datetime.timedelta(minutes=15)
        hours.append(start_time.time())

    # insertamos total de pax reservados de dia
    total_pax = Booking.objects.filter(date__year=year, date__month=month, date__day=day).values('pax').aggregate(
        number_pax=Sum('pax'))
    result = total_pax["number_pax"]
    if result is None:
        result = 0

    # instertamos fecha de dia en cabezera
    date_for_head = (day + ' ' + calendar.month_name[int(month)] + ' ' + year)

    # fecha de dia para usar depues en reservas nuevas
    date_of_day = (year + '-' + month + '-' + day)

    all_booking_of_day = Booking.objects.filter(date__year=year, date__month=month, date__day=day).order_by('time')

    return render(request, 'calendario/day.html',
                  {'result': result, 'date_of_day': date_of_day, 'date_for_head': date_for_head,
                   'all_booking_of_day': all_booking_of_day,
                   'hours': hours, 'day': day, 'month': month})


def new_booking(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        date = datetime.datetime.strptime(request.GET['date'], "%Y-%m-%d").date()
        hour = request.GET['hour']
        time = datetime.datetime.strptime(hour, '%H:%M').time().strftime('%H:%M')
        form = PostForm(initial={'date': date, 'time': time,})

        # date = datetime.date();
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


def post_edit(request, pk):
    post = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)
    return render(request, 'calendario/edit_booking.html', {'form': form})


def getsunday(request):
    return render(request, 'calendario/sunday.html')


def getmonday(request):
    return render(request, 'calendario/monday.html')
