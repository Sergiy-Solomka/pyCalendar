from django.db import models


class Booking(models.Model):
    TIME_CHOICES = (
        ('18:00', '18:00'),
        ('18:15', '18:15'),
        ('18:30', '18:30'),
        ('18:45', '18:45'),
        ('19:00', '19:00'),
        ('19:15', '19:15'),
        ('19:30', '19:30'),
        ('19:45', '19:45'),
        ('20:00', '20:00'),
        ('20:15', '20:15'),
        ('20:30', '20:30'),
        ('20:45', '20:45'),
        ('21:00', '21:00'),
        ('21:15', '21:15'),
        ('21:30', '21:30'),
        )
    date = models.DateField()
    time = models.CharField(max_length =5,choices=TIME_CHOICES)
    pax = models.IntegerField(default=0)
    name = models.CharField(default='',max_length=20)
    table = models.IntegerField(default=0)
    comments = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.date) + ' -- ' + str(self.time) + ' -- Pax: ' + str(self.pax) + ' -- Name: ' + self.name + ' -- Table: ' + str(self.table) + ' -- (' + self.comments + ')'
