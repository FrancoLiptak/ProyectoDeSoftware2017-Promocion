from django.http import HttpResponseRedirect
from apps.health_control.forms import CreateHealthControlForm, UpdateHealthControlForm
from apps.health_control.models import HealthControl
from apps.patient.models import Patient
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

class HealthControlList(PermissionRequiredMixin, ListView):
    permission_required = 'health_control.health_control_list'
    permission_denied_message = 'Acceso denegado. No posees permiso para listar la historia clinica. Contacta a tu administrador'
    raise_exception = True
    model = HealthControl 
    template_name = 'health_control/list.html'

    def get_queryset(self):
        return HealthControl.objects.filter(patient=self.kwargs['patient_id'])

    def get_context_data(self, **kwargs):
        context = super(HealthControlList, self).get_context_data(**kwargs)
        context['patient_id'] = self.kwargs['patient_id']
        return context

class HealthControlCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'health_control.health_control_update'
    permission_denied_message = 'Acceso denegado. No posees permiso para crear el control de salud. Contacta a tu administrador'
    raise_exception = True
    model = HealthControl
    form_class = CreateHealthControlForm
    template_name = 'health_control/form.html'

    def get_context_data(self, **kwargs):
        context = super(HealthControlCreate, self).get_context_data(**kwargs)
        context['header'] = 'Crear nuevo control medico'
        return context

    def get_success_url(self):
        return reverse_lazy('health_control:health_control_list', kwargs={'patient_id': self.object.patient.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST) #Tomo valores de formulario 1
        if form.is_valid(): 
            health_control = form.save(commit=False) 
            health_control.patient = Patient.objects.get(pk=self.kwargs['patient_id'])
            health_control.user = request.user
            health_control.age = health_control.date - health_control.patient.birthday
            health_control.save() #Guardamos todo
            self.object = health_control
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form)) #Devolvemos formularios en blanco
    
class HealthControlUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'health_control.health_control_update'
    permission_denied_message = 'Acceso denegado. No posees permiso para actualizar el control de salud. Contacta a tu administrador'
    raise_exception = True
    model = HealthControl
    form_class = UpdateHealthControlForm
    template_name = 'health_control/form.html'

    def get_success_url(self):
        return reverse_lazy('health_control:health_control_list', kwargs={'patient_id': self.object.patient.id})

    def get_context_data(self, **kwargs):
        context = super(HealthControlUpdate, self).get_context_data(**kwargs)
        context['header'] = 'Actualizar control medico'
        return context            

    def form_valid(self, form):
        self.object.age = (form.cleaned_data['date'] - self.object.patient.birthday).days
        return super(HealthControlUpdate, self).form_valid(form)

class HealthControlDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'health_control.health_control_destroy'
    permission_denied_message = 'Acceso denegado. No posees permiso para borrar el control de salud. Contacta a tu administrador'
    raise_exception = True
    model = HealthControl
    template_name = 'health_control/delete.html'

    def get_success_url(self):
        return reverse_lazy('health_control:health_control_list', kwargs={'patient_id': self.object.patient.id})

class HealthControlShow(PermissionRequiredMixin, DetailView):
    permission_required = 'health_control.health_control_show'
    permission_denied_message = 'Acceso denegado. No posees permiso para ver el control de salud. Contacta a tu administrador'
    raise_exception = True
    model = HealthControl
    template_name = 'health_control/show.html'