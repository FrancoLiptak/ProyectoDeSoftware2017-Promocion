from django import forms
from apps.health_control.models import HealthControl

class CreateHealthControlForm(forms.ModelForm):
    class Meta:
        
        model = HealthControl
        fields = (
            'weight',
            'height',
            'vaccines',
            'vaccines_obs',
            'maturation',
            'maturation_obs',
            'phisical_exam',
            'phisical_exam_obs',
            'pc',
            'ppc',
            'feeding',
            'observations',
        )
        labels = {
            'weight': 'Peso',
            'height': 'Talla',
            'vaccines': '¿Vacunas completas?',
            'vaccines_obs': 'Vacunas observaciones',
            'maturation': '¿Maduración acorde?',
            'maturation_obs': 'Maduración observaciones',
            'phisical_exam': '¿Exámen físico normal?',
            'phisical_exam_obs': 'Exámen físico observaciones',
            'pc': 'PC',
            'ppc': 'PPC',
            'feeding': 'Alimentación',
            'observations': 'Observaciones generales',
        }

class UpdateHealthControlForm(forms.ModelForm):
    class Meta:
        
        model = HealthControl
        fields = (
            'date',
            'weight',
            'height',
            'vaccines',
            'vaccines_obs',
            'maturation',
            'maturation_obs',
            'phisical_exam',
            'phisical_exam_obs',
            'pc',
            'ppc',
            'feeding',
            'observations',
            'user',
        )
        labels = {
            'date': 'Fecha',
            'weight': 'Peso',
            'height': 'Talla',
            'vaccines': '¿Vacunas completas?',
            'vaccines_obs': 'Vacunas observaciones',
            'maturation': '¿Maduración acorde?',
            'maturation_obs': 'Maduración observaciones',
            'phisical_exam': '¿Exámen físico normal?',
            'phisical_exam_obs': 'Exámen físico observaciones',
            'pc': 'PC',
            'ppc': 'PPC',
            'feeding': 'Alimentación',
            'observations': 'Observaciones generales',
            'user': 'Pediatra',
        }