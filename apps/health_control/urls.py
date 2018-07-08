from django.urls import include, path
from apps.health_control.views import * 
from django.contrib.auth.decorators import login_required

app_name = 'health_control'
urlpatterns = [
    path('list/(?P<patient_id>\d+)/', login_required(HealthControlList.as_view()), name='health_control_list'),
    path('create/(?P<patient_id>\d+)/', login_required(HealthControlCreate.as_view()), name='health_control_create'),
    path('update/<pk>/', login_required(HealthControlUpdate.as_view()), name='health_control_update'),
    path('delete/<pk>/', login_required(HealthControlDelete.as_view()), name='health_control_delete'),
    path('show/<pk>/', login_required(HealthControlShow.as_view()), name='health_control_show'),
]