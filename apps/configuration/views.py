from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, CreateView
from apps.configuration.forms import ConfigurationForm, MaintenanceForm
from apps.configuration.models import Configuration
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from maintenance_mode.core import get_maintenance_mode, set_maintenance_mode
from django.core.management import call_command
from django.core.management.base import BaseCommand

class ConfigurationUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'configuration.configuration_update'
    permission_denied_message = 'Acceso denegado. No posees permiso para actualizar la configuracion. Contacta a tu administrador'
    raise_exception = True

    model = Configuration
    form_class = ConfigurationForm
    second_form_class = MaintenanceForm
    template_name = 'configuration/configuration_form.html'
    success_url = reverse_lazy('configuration:configuration')

    def get_object(self):
        return Configuration.objects.all()[:1].get()

    def get_context_data(self, **kwargs):
        context = super(ConfigurationUpdate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context: 
            context['form2'] = self.second_form_class(initial={'maintenance': get_maintenance_mode()}) # Los mensajes de error se van si saco ese self.request.GET
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST, instance=self.get_object()) #Tomo valores de formulario 1 (configuration)
        form2 = self.second_form_class(request.POST) #Tomo valores de formulario 2 (mantenimiento)
        if form.is_valid() and form2.is_valid(): 
            call_command('maintenance_mode', 'on' if form2.cleaned_data['maintenance'] else 'off')
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2)) #Devolvemos formularios en blanco
    
    