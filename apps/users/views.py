from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from apps.users.forms import RegisterUserForm, UpdateUserForm
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from maintenance_mode.core import get_maintenance_mode

class RegisterUser(PermissionRequiredMixin, CreateView):

    permission_required = 'auth.user_update'
    permission_denied_message = 'Acceso denegado. No posees permiso para registrar usuarios. Contacta a tu administrador'
    raise_exception = True

    model = User
    template_name = "users/register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("users:users_list")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST) #Tomo valores de formulario
        if form.is_valid(): 
            patient = form.save(commit=False)
            patient.save() #Guardamos todo
            patient.groups.add(*form.cleaned_data['group'])
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form)) #Devolvemos formularios en blanco

class UsersList(PermissionRequiredMixin, ListView):
    permission_required = 'auth.user_index'
    permission_denied_message = 'Acceso denegado. No posees permiso para listar usuarios. Contacta a tu administrador'
    raise_exception = True
    
    model = User
    template_name = 'users/list.html'

class UsersShow(PermissionRequiredMixin, DetailView):
    permission_required = 'auth.user_index'
    permission_denied_message = 'Acceso denegado. No posees permiso para ver el perfil de los usuarios. Contacta a tu administrador'
    raise_exception = True

    model = User
    template_name = 'users/show.html'

class UsersDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'auth.user_destroy'
    permission_denied_message = 'Acceso denegado. No posees permiso para borrar usuarios. Contacta a tu administrador'
    raise_exception = True
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users:users_list')

class UsersUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'auth.user_update'
    permission_denied_message = 'Acceso denegado. No posees permiso para actualizar usuarios. Contacta a tu administrador'
    raise_exception = True
    model = User
    form_class = UpdateUserForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users:users_list')

    def get_initial(self):
        initial = super(UsersUpdate, self).get_initial()
        try:
            current_groups = self.object.groups.all()
        except:
            # exception can occur if the edited user has no groups
            # or has more than one group
            pass
        else:
            initial['group'] = current_groups
        return initial

    def form_valid(self, form):
        self.object.groups.clear()
        self.object.groups.add(*form.cleaned_data['group'])
        return super(UsersUpdate, self).form_valid(form)

def logued_user(request):
    if get_maintenance_mode():
        return redirect(reverse_lazy('configuration:configuration'))                
    else:
        return redirect(reverse_lazy('patient:patient_index'))