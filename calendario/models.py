from django.db import models


class Booking(models.Model):
    TIME_CHOICES = (
        ('6:00', '6:00'),
        ('6:15', '6:15'),
        ('6:30', '6:30'),
        ('6:45', '6:45'),
        ('7:00', '7:00'),
        ('7:15', '7:15'),
        ('7:30', '7:30'),
        ('7:45', '7:45'),
        ('8:00', '8:00'),
        ('8:15', '8:15'),
        ('8:30', '8:30'),
        ('8:45', '8:45'),
        ('9:00', '9:00'),
        ('9:15', '9:15'),
        ('9:30', '9:30'),
        )
    date = models.DateField()
    time = models.CharField(max_length =5,choices=TIME_CHOICES)
    pax = models.IntegerField(default=0)
    name = models.CharField(default='',max_length=20)
    table = models.IntegerField(default=0)
    comments = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.date) + ' -- ' + str(self.time) + ' -- Pax: ' + str(self.pax) + ' -- Name: ' + self.name + ' -- Table: ' + str(self.table) + ' -- (' + self.comments + ')'
