from django.contrib import admin
from . models import PossibleAppointments, ReservatedAppointments

# Register your models here.

admin.site.register(PossibleAppointments)
admin.site.register(ReservatedAppointments)