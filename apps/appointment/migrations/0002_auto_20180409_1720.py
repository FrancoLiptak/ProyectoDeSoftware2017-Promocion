# Generated by Django 2.0.4 on 2018-04-09 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservatedappointments',
            unique_together={('day', 'time')},
        ),
    ]
