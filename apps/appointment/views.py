from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import ReservatedAppointments, PossibleAppointments
from . serializers import ReservatedAppointmentsSerializer, PossibleAppointmentsSerializer

class AppointmentsList(APIView):

    def get(self, request, format=None):
        date_arg = request.GET.get('date', '')
        possible_appointments = PossibleAppointments.objects.exclude(time__in=(ReservatedAppointments.objects.filter(day = date_arg).values('time')))
        serializer = PossibleAppointmentsSerializer(possible_appointments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        dni_arg = request.GET.get('dni', '')
        date_arg = request.GET.get('date', '')
        time_arg = request.GET.get('time', '')
        serializer = ReservatedAppointmentsSerializer(data={'documentNumber': dni_arg, 'day': date_arg, 'time': time_arg})
        if serializer.is_valid():
            serializer.save()
            return Response(data="Se ha reservado el turno con los siguientes datos: Numero de documento: "+dni_arg+". Fecha: "+date_arg+". Hora: "+time_arg+".")
        return Response(data="Ha habido un problema. Por favor, intente nuevamente.")
