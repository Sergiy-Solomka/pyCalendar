import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Sum

from calendario.forms import PostForm
from .models import Booking

import datetime


def index(request):
    return render(request, 'calendario/month.html')


def get_day_events(request):
    month = request.GET['month']
    year = request.GET['year']
    day = request.GET['day']

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

    all_booking_of_day = Booking.objects.filter(date__year=year, date__month=month, date__day=day).order_by('time')

    return render(request, 'calendario/day.html',
              {'result': result, 'all_booking_of_day': all_booking_of_day, 'hours': hours})


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
