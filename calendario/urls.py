from django.conf.urls import url

from calendario.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^getmonthevents', get_month_bookings, name='monthevents'),
    url(r'^getdayevents', get_day_events, name='dayevents'),
    url(r'^newbooking', new_booking, name='new_booking'),
    url(r'^sundaynewbooking', new_booking_sunday, name='new_booking_sunday'),
    url(r'^booking/(?P<pk>\d+)/edit/$', booking_edit, name='booking_edit'),
    url(r'^sundaybooking/(?P<pk>\d+)/edit/$', booking_edit_sunday, name='booking_edit_sunday'),
]
