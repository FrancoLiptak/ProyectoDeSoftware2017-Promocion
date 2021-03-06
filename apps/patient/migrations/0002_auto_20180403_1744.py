# Generated by Django 2.0.3 on 2018-04-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datademographic',
            name='heating',
            field=models.CharField(choices=[('Gas', 'Gas'), ('Leña', 'Leña'), ('Electrica', 'Electrica')], max_length=15),
        ),
        migrations.AlterField(
            model_name='datademographic',
            name='pet',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='datademographic',
            name='typeOfHousing',
            field=models.CharField(choices=[('Material', 'Material'), ('Chapa', 'Chapa'), ('Madera', 'Madera')], max_length=15),
        ),
        migrations.AlterField(
            model_name='datademographic',
            name='typeOfWater',
            field=models.CharField(choices=[('Corriente', 'Corriente'), ('De Pozo', 'De Pozo')], max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='patient',
            name='documentType',
            field=models.CharField(choices=[('DNI', 'DNI'), ('LC', 'LC'), ('CI', 'CI'), ('LE', 'LE')], max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='healthInsurance',
            field=models.CharField(choices=[('IOMA', 'IOMA'), ('OSDE', 'OSDE'), ('OSECAC', 'OSECAC')], max_length=15),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=35),
        ),
    ]
