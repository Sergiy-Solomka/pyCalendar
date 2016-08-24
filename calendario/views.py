import calendar
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum

from calendario.forms import PostForm
from calendario.forms import PostFormSunday
from .models import Booking
from .models import Table
from .models import SundayBooking

import datetime


def index(request):
    return render(request, 'calendario/month.html')


hollydays_days = ['2017-1-1',  # 1st of Jan
                  '2016-12-26',  # Boxing day
                  '2016-8-22', '2016-8-23', '2016-8-24', '2016-8-25', '2016-8-26', '2016-8-27', '2016-8-28'
                  # Rest Hollydays
                  ]

days_off = ['Monday']

# Dias cuando estemos abiertos aun que sea dia libre.
exeption_days = ['2017-12-31',  # New year
                 '2017-2-14',  # San Valentin
                 ]


def get_day_events(request):
    month = request.GET['month']
    year = request.GET['year']
    day = request.GET['day']
    weekdayname = request.GET['weekdayname']

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

    # List of tables what still avelible for boking

    tables_list = list(Table.objects.all().values('name'))
    tables_list_2 = [f['name'] for f in tables_list]
    tables_list_2 = [int(i) for i in tables_list_2]

    tables_booked = list(Booking.objects.filter(date__year=year, date__month=month, date__day=day).values('tables'))
    tables_booked_2 = [f['tables'] for f in tables_booked]

    vacancy_1 = list(set(tables_list_2) - set(tables_booked_2))
    vacancy = sorted(vacancy_1, key=int)

    # fecha de dia para usar depues en reservas nuevas
    date_of_day = (year + '-' + month + '-' + day)

    all_booking_of_day = Booking.objects.filter(date__year=year, date__month=month, date__day=day).order_by('time')
    all_booking_of_sunday = SundayBooking.objects.filter(date__year=year, date__month=month, date__day=day).order_by(
        'time')

    # Vamos comprobar que los dias no sean dias libres o dias de vacaciones y  idas de exepciones

    for i in hollydays_days:
        if i == date_of_day:
            return render(request, 'calendario/hollydays.html')

    for i in days_off:
        if i == weekdayname:
            return render(request, 'calendario/dayoff.html')

    for i in exeption_days:
        if i == date_of_day:
            return render(request, 'calendario/day.html',
                          {'result': result, 'date_of_day': date_of_day,
                           'all_booking_of_day': all_booking_of_day,
                           'hours': hours, 'vacancy': vacancy,
                           'booking_day': datetime.datetime(day=int(day), month=int(month), year=int(year)).date()})

    if weekdayname == "Sunday":
        # insertamos total de pax reservados de sunday
        total_pax_sunday = SundayBooking.objects.filter(date__year=year, date__month=month, date__day=day).values(
            'pax').aggregate(
            number_pax=Sum('pax'))
        result_sunday = total_pax_sunday["number_pax"]

        sunday_bookings_first = [['13:00', 1],
                                 ['13:00', 2],
                                 ['13:00', 3],
                                 ['13:00', 4],
                                 ['13:00', 5],
                                 ['13:00', 105],
                                 ['13:15', 6],
                                 ['13:15', 8],
                                 ['13:15', 9],
                                 ['13:15', 10],
                                 ['13:30', 12],
                                 ['13:30', 14],
                                 ['13:30', 15],
                                 ['13:30', 115],
                                 ['13:45', 16],
                                 ['13:45', 116],
                                 ['13:45', 17],
                                 ['13:45', 18],
                                 ['13:45', 19],
                                 ['13:45', 20],
                                 ['14:00', 21],
                                 ['14:00', 22],
                                 ['14:00', 23],
                                 ['14:00', 30],
                                 ['14:00', 31],
                                 ['14:00', 32],
                                 ['14:00', 33],
                                 ['14:00', 34],
                                 ]

        sunday_bookings_second = [['15:30', 1],
                                  ['15:45', 2],
                                  ['15:45', 3],
                                  ['15:30', 4],
                                  ['15:45', 5],
                                  ['15:45', 105],
                                  ['15:45', 6],
                                  ['15:30', 8],
                                  ['15:45', 9],
                                  ['15:45', 10],
                                  ['16:00', 12],
                                  ['16:00', 14],
                                  ['16:15', 15],
                                  ['16:15', 115],
                                  ['16:15', 16],
                                  ['16:15', 116],
                                  ['16:15', 17],
                                  ['16:15', 18],
                                  ['16:30', 19],
                                  ['16:30', 20],
                                  ['16:30', 21],
                                  ['16:30', 22],
                                  ['16:30', 23],
                                  ['16:30', 30],
                                  ['16:30', 31],
                                  ['16:30', 32],
                                  ['16:30', 33],
                                  ['16:30', 34],
                                  ]

        if result_sunday is None:
            result_sunday = 0
        return render(request, 'calendario/sunday.html',
                      {'result_sunday': result_sunday, 'date_of_day': date_of_day,
                       'all_booking_of_sunday': all_booking_of_sunday, 'sunday_bookings_first': sunday_bookings_first,
                       'sunday_bookings_second': sunday_bookings_second,
                       'booking_day': datetime.datetime(day=int(day), month=int(month), year=int(year)).date()})

    return render(request, 'calendario/day.html',
                  {'result': result, 'date_of_day': date_of_day,
                   'all_booking_of_day': all_booking_of_day,
                   'hours': hours, 'vacancy': vacancy,
                   'booking_day': datetime.datetime(day=int(day), month=int(month), year=int(year)).date()})


def new_booking_sunday(request):
    if request.method == "POST":
        form = PostFormSunday(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()  # save model relations (tables)
            # TODO: make a better redirect
            return redirect(request.GET.get('returnurl') or 'index')  # redirect to index if no url specified
    else:
        date = datetime.datetime.strptime(request.GET['date'], "%Y-%m-%d").date()
        hour = request.GET['hour']
        time = datetime.datetime.strptime(hour, '%H:%M').time().strftime('%H:%M')
        tables = request.GET['table']
        form = PostFormSunday(initial={'date': date, 'time': time, 'tables': tables})

    return render(request, 'calendario/new_booking.html', {'form': form})


def booking_edit_sunday(request, pk):
    post = get_object_or_404(SundayBooking, pk=pk)
    if request.method == "POST":
        form = PostFormSunday(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()
            return redirect('index')  # TODO: make a better redirect
    else:
        form = PostFormSunday(instance=post)
    return render(request, 'calendario/edit_booking.html', {'form': form})


def new_booking(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()  # save model relations (tables)
            # TODO: make a better redirect
            return redirect(request.GET.get('returnurl') or 'index')  # redirect to index if no url specified
    else:
        date = datetime.datetime.strptime(request.GET['date'], "%Y-%m-%d").date()
        hour = request.GET['hour']
        time = datetime.datetime.strptime(hour, '%H:%M').time().strftime('%H:%M')
        form = PostForm(initial={'date': date, 'time': time})

    return render(request, 'calendario/new_booking.html', {'form': form})


def get_month_bookings(request):
    if request.is_ajax():
        month = request.GET['month']
        year = request.GET['year']

        result_week = Booking.objects.filter(date__year=year, date__month=month).values('date').annotate(
            number_of_bookings=Sum('pax'))
        result_sunday = SundayBooking.objects.filter(date__year=year, date__month=month).values('date').annotate(
            number_of_bookings=Sum('pax'))

        response = {}
        for item in list(result_week):
            response[item['date'].strftime('%m-%d-%Y')] = item['number_of_bookings']
        for item in list(result_sunday):
            response[item['date'].strftime('%m-%d-%Y')] = item['number_of_bookings']

        return HttpResponse(json.dumps(response))


def booking_edit(request, pk):
    post = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()
            return redirect('index')  # TODO: make a better redirect
    else:
        form = PostForm(instance=post)
    return render(request, 'calendario/edit_booking.html', {'form': form})
