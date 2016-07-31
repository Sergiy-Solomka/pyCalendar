from django.core.exceptions import ValidationError
from django.db import models
from multiselectfield import MultiSelectField


class Booking(models.Model):
    TABLE_CHOICES = (
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('105', '105'),
        ('06', '06'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('12', '12'),
        ('14', '14'),
        ('15', '15'),
        ('115', '115'),
        ('16', '16'),
        ('116', '116'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
    )
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

    def validate_name(self):
        if True:
            raise ValidationError(('sex'), code='invalid')

    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_CHOICES)
    pax = models.IntegerField(default=0)
    name = models.CharField(default='', max_length=20, validators=[validate_name])
    table = MultiSelectField(choices=TABLE_CHOICES,
                             max_choices=20,
                             max_length=30)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.date) + ' -- ' + str(self.time) + ' -- Pax: ' + str(
            self.pax) + ' -- Name: ' + self.name + ' -- Table: ' + str(self.table) + ' -- (' + self.comments + ')'
