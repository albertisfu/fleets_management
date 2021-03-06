# Generated by Django 4.0.1 on 2022-01-09 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.IntegerField(verbose_name='Vehicle ID')),
                ('fuel_level', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Fuel Level')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_location', models.IntegerField(choices=[(0, 'city_a'), (1, 'city_b'), (2, 'city_c')], default=0, verbose_name='Current location')),
                ('distance_traveled', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Travel Distance KM')),
                ('fuel_consumed', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Fuel Consumed LT')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.vehicle', verbose_name='Vehicle')),
            ],
        ),
    ]
