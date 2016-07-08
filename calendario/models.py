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


class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField(default=0)
    pax = models.IntegerField(default=0)
    name = models.CharField(default='',max_length=10)
    table = models.IntegerField(default=0)
    comments = models.TextField()

    def __str__(self):
        return str(self.date) + ' -- ' + str(self.time) + ' -- Pax: ' + str(self.pax) + ' -- Name: ' + self.name + ' -- Table: ' + str(self.table) + ' -- (' + self.comments + ')'
