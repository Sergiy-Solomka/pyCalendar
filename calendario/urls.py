from django.conf.urls import url

from calendario.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^getmonthevents', get_month_bookings, name='monthevents'),
    url(r'^getdayevents', get_day_events, name='dayevents'),
    url(r'^newbooking', new_booking, name='new_booking'),
    url(r'^post/(?P<pk>\d+)/edit/$', post_edit, name='post_edit'),
    url(r'^getsunday', getsunday, name='getsunday'),
    url(r'^getmonday', getmonday, name='getmonday'),

]
