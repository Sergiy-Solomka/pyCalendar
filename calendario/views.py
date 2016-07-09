import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count

from calendario.forms import PostForm
from .models import Booking


def index(request):
    return render(request, 'calendario/month.html')


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


def get_day_events(request):
    return render(request, 'calendario/day.html')


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
