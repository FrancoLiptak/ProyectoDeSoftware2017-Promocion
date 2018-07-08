from django.urls import include, path
from apps.configuration.views import * 
from django.contrib.auth.decorators import login_required

app_name = 'configuration'
urlpatterns = [
    path('', login_required(ConfigurationUpdate.as_view()), name='configuration'),

]