from django.conf.urls import url

from calendario.views import index, get_day_events, get_month_bookings,new_booking,post_edit
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^getmonthevents', get_month_bookings, name='monthevents'),
    url(r'^getdayevents', get_day_events, name='dayevents'),
    url(r'^newbooking', new_booking, name='new_booking'),
    url(r'^post/(?P<pk>\d+)/edit/$', post_edit, name='post_edit'),

]
