from django.db import models


class Event(models.Model):
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return str(self.date) + ' ' + str(self.start) + ' - ' + str(self.end) + ' ' + self.description


class Table(models.Model):
    name = models.TextField()
    capacity = models.IntegerField()
