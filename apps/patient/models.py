from django.db import models
from django.core.validators import MinValueValidator
from apps.patient.ResourceCollector import ResourceCollector
from django.core.validators import RegexValidator

class DataDemographic(models.Model):
    fridge = models.CharField(max_length=2, choices=(('Si', 'Si'), ('No', 'No')))
    heating = models.CharField(max_length=25, choices=(ResourceCollector.getTypeOfResource("https://api-referencias.proyecto2017.linti.unlp.edu.ar/tipo-calefaccion")))
    electricity = models.CharField(max_length=2, choices=(('Si', 'Si'), ('No', 'No')))
    typeOfHousing = models.CharField(max_length=25, choices=(ResourceCollector.getTypeOfResource("https://api-referencias.proyecto2017.linti.unlp.edu.ar/tipo-vivienda")))
    pet = models.CharField(max_length=2, choices=(('Si', 'Si'), ('No', 'No')))
    typeOfWater = models.CharField(max_length=25, choices=(ResourceCollector.getTypeOfResource("https://api-referencias.proyecto2017.linti.unlp.edu.ar/tipo-agua")))
    
class Patient(models.Model):
    letters = RegexValidator(r'^[a-zA-Z ]+$', 'Solo se permite ingresar letras.')
    lastName = models.CharField(max_length=50, validators=[letters])
    name = models.CharField(max_length=50, validators=[letters])
    birthday = models.DateField()
    documentType = models.CharField(max_length=15, choices=(ResourceCollector.getTypeOfResource("https://api-referencias.proyecto2017.linti.unlp.edu.ar/tipo-documento")))
    documentNumber = models.IntegerField(validators=[MinValueValidator(500000)])
    address = models.CharField(max_length=80)
    phone = models.CharField(max_length=15)
    healthInsurance = models.CharField(max_length=15, choices=(ResourceCollector.getTypeOfResource("https://api-referencias.proyecto2017.linti.unlp.edu.ar/obra-social")))
    gender = models.CharField(max_length=15, choices=(('Masculino', 'Masculino'), ('Femenino', 'Femenino')))
    dataDemographic = models.OneToOneField(DataDemographic, null=True, blank=True, on_delete=models.CASCADE)