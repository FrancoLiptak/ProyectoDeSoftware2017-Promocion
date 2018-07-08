from rest_framework import serializers
from apps.appointment.models import PossibleAppointments, ReservatedAppointments # aca iba otra cosa

class PossibleAppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PossibleAppointments
        fields = '__all__'

class ReservatedAppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservatedAppointments
        fields = ('documentNumber', 'day', 'time')

        def create(self, validated_data):
            documentNumber = validated_data.get('documentNumber', None)
            day = validated_data.get('day', None)
            time = validated_data.get('time', None)
            return ReservatedAppointments.objects.create(documentNumber=documentNumber, day=day, time=time)

