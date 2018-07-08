from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.patient.models import DataDemographic, Patient
from apps.health_control.models import HealthControl
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from collections import Counter
import pandas as pd

class DDReport(PermissionRequiredMixin, View):
    permission_required = 'patient.dataDemographic_show'
    permission_denied_message = 'Acceso denegado. No posees permiso para ver el reporte de datos demograficos. Contacta a tu administrador'
    raise_exception = True

    template_name = 'report/dd_report.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = {}
        # Add in the average of all de demographic data
        context['averageElectricity'] = self.getAverage(
            DataDemographic.objects.values_list('electricity', flat=True))
        context['averageFridge'] = self.getAverage(
            DataDemographic.objects.values_list('fridge', flat=True))
        context['averageLivingPlace'] = self.getAverage(
            DataDemographic.objects.values_list('typeOfHousing', flat=True))
        context['averageHeating'] = self.getAverage(
            DataDemographic.objects.values_list('heating', flat=True))
        context['averageWater'] = self.getAverage(
            DataDemographic.objects.values_list('typeOfWater', flat=True))
        context['averagePet'] = self.getAverage(
            DataDemographic.objects.values_list('pet', flat=True))
        return context

    def getAverage(self, dataArray, apiUrl=None):
        answer = []
        #efficient count
        count = Counter(dataArray).items()
        for key, value in count:
            answer.append({'name': key, 'value': value/len(dataArray)*100})
        return answer

class PatientReport(PermissionRequiredMixin, View):
    permission_required = 'health_control.health_control_list'
    permission_denied_message = 'Acceso denegado. No posees permiso para ver el reporte de datos del paciente. Contacta a tu administrador'
    raise_exception = True

    template_name = 'report/patient_report.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = {}
        patient = Patient.objects.get(id=self.kwargs['patient_id'])
        controls = HealthControl.objects.filter(patient=patient)
        context['controls'] = controls
        context['patient'] = patient
        context.update(self.getAverages(patient.gender))
        return context

    def getAverages(self, gender):

        urlGrowthMale = 'http://www.who.int/childgrowth/standards/tab_wfa_boys_p_0_13.txt'
        urlGrowthFemale = 'http://www.who.int/childgrowth/standards/wfa_girls_0_13_zscores.txt'
        urlHeightMale = 'http://www.who.int/childgrowth/standards/tab_lhfa_boys_p_0_2.txt'
        urlHeightFemale = 'http://www.who.int/childgrowth/standards/tab_lhfa_girls_p_0_2.txt'
        urlPpcMale = 'http://www.who.int/childgrowth/standards/second_set/tab_hcfa_boys_p_0_13.txt'
        urlPpcFemale = 'http://www.who.int/childgrowth/standards/second_set/tab_hcfa_girls_p_0_13.txt'            

        def maleGrowthMapper(row): return {
            'x':row[0],
            'y1':row[6],
            'y2':row[9],
            'y3':row[11],
            'y4':row[13],
            'y5':row[16]}

        def femaleGrowthMapper(row): return {
            'x':row[0],
            'y1':row[5],
            'y2':row[6],
            'y3':row[7],
            'y4':row[8],
            'y5':row[9]}

        def heightOrPpcMapper(row): return {
            'x':row[0],
            'y1':row[7],
            'y2':row[10],
            'y3':row[12],
            'y4':row[14],
            'y5':row[17]}

        answer = {}
        if(gender=='Masculino'):
            answer['averageGrowth'] = self.getPatientsAverage(
                pd.read_csv(urlGrowthMale, delimiter="\t"), maleGrowthMapper)
            answer['averageHeight'] = self.getPatientsAverage(
                pd.read_csv(urlHeightMale, delimiter="\t"), heightOrPpcMapper)
            answer['averagePpc'] = self.getPatientsAverage(
                pd.read_csv(urlPpcMale, delimiter="\t"), heightOrPpcMapper)
        else:
            answer['averageGrowth'] = self.getPatientsAverage(
                pd.read_csv(urlGrowthFemale, delimiter="\t"), femaleGrowthMapper)
            answer['averageHeight'] = self.getPatientsAverage(
                pd.read_csv(urlHeightFemale, delimiter="\t"), heightOrPpcMapper)
            answer['averagePpc'] = self.getPatientsAverage(
                pd.read_csv(urlPpcFemale, delimiter="\t"), heightOrPpcMapper)
        return answer

    def getPatientsAverage(self, df, mapper):
        answer = []
        for index, row in df.iterrows():
            answer.append(mapper(row))
        return answer