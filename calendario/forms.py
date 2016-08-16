from django import forms

from calendario.models import Booking, SundayBooking


class PostForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date', 'time', 'pax', 'name', 'tables', 'comments', 'phone')


class PostFormSunday(forms.ModelForm):
    class Meta:
        model = SundayBooking
        fields = ('date', 'time', 'pax', 'name', 'tables', 'comments', 'phone')
