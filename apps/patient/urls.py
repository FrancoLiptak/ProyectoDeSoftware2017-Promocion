from django.urls import include, path
from apps.patient.views import * 
from django.contrib.auth.decorators import login_required

app_name = 'patient'
urlpatterns = [
    path('index', login_required(PatientList.as_view()), name='patient_index'),
    path('create', login_required(PatientCreate.as_view()), name='patient_create'),
    path('update/<pk>/', login_required(PatientUpdate.as_view()), name='patient_update'),
    path('delete/<pk>/', login_required(PatientDelete.as_view()), name='patient_delete'),
    path('show/<pk>/', login_required(PatientShow.as_view()), name='patient_show'),
]