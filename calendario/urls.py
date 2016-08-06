from django.conf.urls import url

from calendario.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^getmonthevents', get_month_bookings, name='monthevents'),
    url(r'^getdayevents', get_day_events, name='dayevents'),
    url(r'^newbooking', new_booking, name='new_booking'),
    url(r'^booking/(?P<pk>\d+)/edit/$', booking_edit, name='booking_edit'),
    url(r'^getsunday/(?P<year>\d{4})/(?P<month>\d{2})/(?P<weekday>\d{1})/(?P<day>\d+)/$', getsunday, name='getsunday'),
    url(r'^getmonday', getmonday, name='getmonday'),

]
