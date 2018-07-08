from django.db import models
from django.core.validators import validate_email, MinValueValidator
from django.core.validators import RegexValidator

class Configuration(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Solo se permiten caracteres alfanuméricos.')

    title = models.CharField(max_length=100, default="Hospital Dr. Ricardo Gutiérrez", validators=[alphanumeric])
    email = models.EmailField(default="info@hospitalgutierrez.com")
    phone = models.CharField(max_length=100, default="0221 483-0171")
    address = models.CharField(max_length=100, default="Diagonal 114 329, La Plata, Buenos Aires")
    description = models.TextField(default="El Hospital Gutierrez de La Plata fue inaugurado el 6 de Agosto de 1954. En ese entonces, el hospital funcionaba solo en el área central del edificio. En 1956, la casa de admisión Dardo Rocha es trasladada para dar lugar al Hogar Materno Infantil “Dra. Cecilia Grierson”, y posteriormente la Casa del Niño Alfredo Palacios. En 1972, el hospital es remodelado y pasa a tener 12 salas de internación y a 172 las camas de dotación. El ala ocupada por Casa del Niño es cedida al hospital en 1987, permitiendo el traslado de la Maternidad y servicio de Pediatría. Más tarde, en 1987, se inaugura el primer piso del ala derecha, contruido anteriormente ese mismo año, siendo ésta la última gran remodelación del hospital.")
    items_per_page = models.IntegerField(validators=[MinValueValidator(1)], default=10)