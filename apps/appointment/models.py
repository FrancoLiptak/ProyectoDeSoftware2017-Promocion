from django.db import models
from django.core.validators import MinValueValidator

class PossibleAppointments(models.Model):
    time = models.TimeField()

class ReservatedAppointments(models.Model):
    documentNumber = models.IntegerField(validators=[MinValueValidator(500000)])
    day = models.DateField()
    time = models.TimeField()

    class Meta:
        unique_together = ('day', 'time',)