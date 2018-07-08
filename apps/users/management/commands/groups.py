from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from apps.configuration.models import Configuration



class Command(BaseCommand):

    def handle(self, *args, **options):
        # creacion de grupos
        recepcionista, created = Group.objects.get_or_create(name='recepcionista')
        pediatra, created = Group.objects.get_or_create(name='pediatra')
        administrador, created = Group.objects.get_or_create(name='administrador')

        # permisos users
        user_ct = ContentType.objects.get(app_label="auth", model="user")
        user_index, created = Permission.objects.get_or_create(name='Can Index User', codename='user_index',
                            content_type=user_ct)
        user_show, created = Permission.objects.get_or_create(name='Can Show User', codename='user_show',
                            content_type=user_ct)
        user_update, created = Permission.objects.get_or_create(name='Can Update User', codename='user_update',
                            content_type=user_ct)
        user_destroy, created = Permission.objects.get_or_create(name='Can Destroy User', codename='user_destroy',
                            content_type=user_ct)
        administrador.permissions.add(user_destroy, user_index, user_show, user_update)

        # permisos configuration
        configuration_ct = ContentType.objects.get_for_model(Configuration)
        configuration_update, created = Permission.objects.get_or_create(name='Can Update Configuration', codename='configuration_update',
                            content_type=configuration_ct)
        administrador.permissions.add(configuration_update)

        # permisos patient
        patient_ct = ContentType.objects.get(app_label='patient', model='patient')
        patient_index, created = Permission.objects.get_or_create(name='Can Index Patient', codename='patient_index',
                            content_type=patient_ct)
        patient_show, created = Permission.objects.get_or_create(name='Can Show Patient', codename='patient_show',
                            content_type=patient_ct)
        patient_update, created = Permission.objects.get_or_create(name='Can Update Patient', codename='patient_update',
                            content_type=patient_ct)
        patient_destroy, created = Permission.objects.get_or_create(name='Can Destroy Patient', codename='patient_destroy',
                            content_type=patient_ct)
        recepcionista.permissions.add(patient_index, patient_show, patient_update)
        pediatra.permissions.add(patient_index, patient_show, patient_update)
        administrador.permissions.add(patient_destroy, patient_index, patient_show, patient_update)

        # permisos datademographic
        dataDemographic_ct = ContentType.objects.get(app_label='patient', model='datademographic')
        dataDemographic_show, created = Permission.objects.get_or_create(name='Can Show DataDemographic', codename='dataDemographic_show',
                            content_type=dataDemographic_ct)
        dataDemographic_update, created = Permission.objects.get_or_create(name='Can Update DataDemographic', codename='dataDemographic_update',
                            content_type=dataDemographic_ct)
        dataDemographic_destroy, created = Permission.objects.get_or_create(name='Can Destroy DataDemographic', codename='dataDemographic_destroy',
                            content_type=dataDemographic_ct)
        recepcionista.permissions.add(dataDemographic_show, dataDemographic_update)
        pediatra.permissions.add(dataDemographic_show, dataDemographic_update)
        administrador.permissions.add(dataDemographic_destroy, dataDemographic_show, dataDemographic_update)

        # permisos health_control
        health_control_ct = ContentType.objects.get(app_label='health_control', model='healthcontrol')
        health_control_list, created = Permission.objects.get_or_create(name='Can List HealthControl', codename='health_control_list',
                            content_type=health_control_ct)
        health_control_show, created = Permission.objects.get_or_create(name='Can Show HealthControl', codename='health_control_show',
                            content_type=health_control_ct)
        health_control_update, created = Permission.objects.get_or_create(name='Can Update HealthControl', codename='health_control_update',
                            content_type=health_control_ct)
        health_control_destroy, created = Permission.objects.get_or_create(name='Can Destroy HealthControl', codename='health_control_destroy',
                            content_type=health_control_ct)
        pediatra.permissions.add(health_control_list, health_control_show, health_control_update)
        administrador.permissions.add(health_control_destroy, health_control_list, health_control_show)