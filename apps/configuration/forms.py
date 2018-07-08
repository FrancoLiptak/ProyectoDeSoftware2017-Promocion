from django import forms
from apps.configuration.models import Configuration
from maintenance_mode.core import get_maintenance_mode, set_maintenance_mode


class ConfigurationForm(forms.ModelForm):
    class Meta:
        model = Configuration
        fields = (
                    'title',
                    'email',
                    'phone',
                    'address',
                    'description',
                    'items_per_page',
                )
        labels = {
            'title': 'Título',
            'email': 'Email',
            'phone': 'Teléfono',
            'address': 'Dirección',
            'description': 'Descripción',
            'items_per_page': 'Cantidad de elementos por página',
        }
        widges = {
            'title': forms.CharField(max_length=100, min_length=1),
            'email': forms.EmailField(),
            'description': forms.CharField(min_length=1),
            'phone': forms.CharField(max_length=100, min_length=1),
            'address': forms.CharField(max_length=100, min_length=1),
        }

        def __init__(self, *args, **kwargs):
            super(PatientForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })
    
class MaintenanceForm(forms.Form):
    maintenance = forms.BooleanField(required=False)  
    class Meta:
        fields = (
                    'maintenance',
                )
        labels = {
            'maintenance': '¿Sitio en mantenimiento?',
        }
