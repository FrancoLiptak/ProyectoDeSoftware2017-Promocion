"""proyecto_hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from apps.patient.views import * 

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('users/', include ('apps.users.urls', namespace="users")),
    path('patient/', include ('apps.patient.urls', namespace="patient")),
    path('configuration/', include ('apps.configuration.urls', namespace="configuration")),
    path(r'^', include('django_telegrambot.urls')),
    path('appointments/', include ('apps.appointment.urls', namespace="appointment")),
    path('health_control/', include ('apps.health_control.urls', namespace="health_control")),
    path('report/', include ('apps.report.urls', namespace="report")),
]
