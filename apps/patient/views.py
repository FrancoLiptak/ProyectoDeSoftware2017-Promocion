from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from apps.patient.forms import PatientForm, DataDemographicForm
from apps.patient.models import Patient, DataDemographic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from maintenance_mode.core import get_maintenance_mode

import requests

class IndexView(TemplateView):
    template_name = 'index/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if get_maintenance_mode():
                return redirect(reverse_lazy('users:users_login'))                
            else:
                return redirect(reverse_lazy('patient:patient_index'))

        return super(IndexView, self).dispatch(request, *args, **kwargs)

class PatientList(PermissionRequiredMixin, ListView):
    permission_required = 'patient.patient_index'
    permission_denied_message = 'Acceso denegado. No posees permiso para listar pacientes. Contacta a tu administrador'
    raise_exception = True

    model = Patient 
    template_name = 'patient/index.html'

    #MyModel.objects.filter(..).update(my_attr=True)

class PatientCreate(PermissionRequiredMixin, CreateView):
    permission_required = ("patient.patient_update", "patient.dataDemographic_update")
    permission_denied_message = 'Acceso denegado. No posees permiso para crear una paciente. Contacta a tu administrador'
    raise_exception = True

    model = Patient
    form_class = PatientForm
    second_form_class = DataDemographicForm
    template_name = 'patient/create.html'
    success_url = reverse_lazy('patient:patient_index')
    
    def get_context_data(self, **kwargs):
        context = super(PatientCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context: #form2 es el formulario de los datos demográficos
            context['form2'] = self.second_form_class() # Los mensajes de error se van si saco ese self.request.GET
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST) #Tomo valores de formulario 1 (patient)
        form2 = self.second_form_class(request.POST) #Tomo valores de formulario 2 (dataDemographic)
        if form.is_valid() and form2.is_valid(): 
            patient = form.save(commit=False) 
            patient.dataDemographic = form2.save() #Creamos las relaciones
            patient.save() #Guardamos todo
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2= form2)) #Devolvemos formularios en blanco

class PatientUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ("patient.patient_update", "patient.dataDemographic_update")
    permission_denied_message = 'Acceso denegado. No posees permiso para actualizar un paciente. Contacta a tu administrador'
    raise_exception = True

    model = Patient
    second_model = DataDemographic
    form_class = PatientForm
    second_form_class = DataDemographicForm
    template_name = 'patient/update.html'
    success_url = reverse_lazy('patient:patient_index')

    def get_context_data(self, **kwargs):
        context = super(PatientUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        patient = self.model.objects.get(id=pk)
        dataDemographic = self.second_model.objects.get(id=patient.dataDemographic_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=dataDemographic)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_patient = kwargs['pk']
        patient = self.model.objects.get(id=id_patient)
        dataDemographic = self.second_model.objects.get(id=patient.dataDemographic_id)
        form = self.form_class(request.POST, instance=patient)
        form2 = self.second_form_class(request.POST, instance=dataDemographic)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())
            

class PatientDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ("patient.patient_destroy", "patient.dataDemographic_destroy")
    permission_denied_message = 'Acceso denegado. No posees permiso para borrar un paciente. Contacta a tu administrador'
    raise_exception = True

    model = Patient
    template_name = 'patient/delete.html'
    success_url = reverse_lazy('patient:patient_index')

class PatientShow(PermissionRequiredMixin, DetailView):
    permission_required = ("patient.patient_show", "patient.dataDemographic_show")
    permission_denied_message = 'Acceso denegado. No posees permiso para ver un paciente. Contacta a tu administrador'
    raise_exception = True

    model = Patient
    template_name = 'patient/show.html'