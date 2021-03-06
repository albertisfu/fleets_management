# Generated by Django 4.0.1 on 2022-01-10 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='fuel_level',
        ),
        migrations.AlterField(
            model_name='vehiclehistory',
            name='current_location',
            field=models.CharField(choices=[('city_a', 'city_a'), ('city_b', 'city_b'), ('city_c', 'city_c')], default='city_a', max_length=20, verbose_name='Current location'),
        ),
        migrations.AlterField(
            model_name='vehiclehistory',
            name='distance_traveled',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=6, verbose_name='Travel Distance KM'),
        ),
        migrations.AlterField(
            model_name='vehiclehistory',
            name='fuel_consumed',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=6, verbose_name='Fuel Consumed LT'),
        ),
    ]
