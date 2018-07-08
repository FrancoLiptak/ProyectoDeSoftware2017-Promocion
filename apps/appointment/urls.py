from django.urls import include, path
from apps.appointment.views import * 

app_name = 'appointment'
urlpatterns = [
    path('turnos/', AppointmentsList.as_view(), name='get_appointments'),
]