from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField()

    def __str__(self):
        return 'Client: ' + self.name + ', Phone: ' + str(self.phone)


class Table(models.Model):
    name = models.CharField(max_length=20)
    capacity = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return 'Table: ' + self.name + ', Capacity: ' + str(self.capacity) + (
            ' (' + self.description + ')' if self.description != '' else '')


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
        ('21:45', '21:45'),
        ('22:00', '22:00')
    )

    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_CHOICES)
    pax = models.IntegerField(default=0)
    name = models.ManyToManyField(Client)
    tables = models.ManyToManyField(Table)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        tables = ''
        first = True
        for table in self.tables.all():
            if first:
                tables = table.name
                first = False
            else:
                tables += ', ' + table.name

        return str(self.date) + ' -- ' + str(self.time) + ' -- Pax: ' + str(
            self.pax) + ' -- Name: ' + str(Client) + ' -- Tables: [' + tables + '] -- (' + self.comments + ')'
