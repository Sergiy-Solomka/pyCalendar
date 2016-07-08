from django.db import models



class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField(default=0)
    pax = models.IntegerField(default=0)
    name = models.CharField(default='',max_length=20)
    table = models.IntegerField(default=0)
    comments = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.date) + ' -- ' + str(self.time) + ' -- Pax: ' + str(self.pax) + ' -- Name: ' + self.name + ' -- Table: ' + str(self.table) + ' -- (' + self.comments + ')'
