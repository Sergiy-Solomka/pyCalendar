from django import forms

from calendario.models import Booking


class PostForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('date', 'time', 'pax', 'name', 'tables', 'comments','phone')
