from django.conf.urls import url

from . import views

app_name = 'calendario'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getmonthevents', views.get_month_events, name='monthevents'),
    url(r'^day', views.day_event, name='dayevent'),
]
