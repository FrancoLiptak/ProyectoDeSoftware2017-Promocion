from django.urls import path
from apps.report.views import * 
from django.contrib.auth.decorators import login_required

app_name = 'report'
urlpatterns = [
    path('', login_required(DDReport.as_view()), name='demographic_data_report'),
    path('(?P<patient_id>\d+)/', login_required(PatientReport.as_view()), name='patient_report'),
]