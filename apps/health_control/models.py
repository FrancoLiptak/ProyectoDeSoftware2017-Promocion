from django.db import models
from django.conf import settings
from apps.patient.models import Patient
from datetime import date

# Create your models here.

class HealthControl(models.Model):
    date = models.DateField(default=date.today)
    age = models.IntegerField()
    weight = models.FloatField()
    vaccines = models.BooleanField()
    vaccines_obs = models.TextField()
    maturation = models.BooleanField()
    maturation_obs = models.TextField()
    phisical_exam = models.BooleanField()
    phisical_exam_obs = models.TextField()
    pc = models.FloatField()
    ppc = models.FloatField()
    height = models.FloatField()
    feeding = models.TextField()
    observations = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'groups__name': 'pediatra'},
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
    )