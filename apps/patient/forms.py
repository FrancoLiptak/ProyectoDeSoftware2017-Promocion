from django import forms
from apps.patient.models import Patient, DataDemographic

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
                    'lastName',
                    'name',
                    'birthday',
                    'documentType',
                    'documentNumber',
                    'address',
                    'phone',
                    'healthInsurance',
                    'gender',
                )
        labels = {
            'lastName': 'Apellido',
            'name': 'Nombre',
            'birthday': 'Fecha de nacimiento (DD/MM/AAAA)',
            'documentType': 'Tipo de documento',
            'documentNumber': 'Número de documento',
            'address': 'Dirección',
            'phone': 'Teléfono',
            'healthInsurance': 'Obra social',
            'gender': 'Género',
        }

        widges = {
            'lastName': forms.CharField(max_length=50, min_length=1),
            'name': forms.CharField(max_length=50, min_length=1),
            'address': forms.CharField(max_length=100, min_length=5),
            'phone': forms.CharField(max_length=30, min_length=6),
        }

        def __init__(self, *args, **kwargs):
            super(PatientForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

class DataDemographicForm(forms.ModelForm):
    class Meta:
        model = DataDemographic
        fields = (
                'fridge',
                'heating',
                'electricity',
                'typeOfHousing',
                'pet',
                'typeOfWater',
                )
        labels = {
            'fridge': 'Heladera',
            'heating': 'Calefacción',
            'electricity': 'Electricidad',
            'typeOfHousing': 'Tipo de vivienda',
            'pet': 'Mascota',
            'typeOfWater': 'Tipo de agua',
        }

        def __init__(self, *args, **kwargs):
            super(DataDemographicForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })