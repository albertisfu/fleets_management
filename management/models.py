from django.db import models
# Create your models here.


class Vehicle(models.Model):
    """
    A model to hold vehicle information.
    """
    vehicle_id = models.IntegerField(verbose_name='Vehicle ID',)

    def __str__(self):
        return str(self.vehicle_id)


class VehicleHistory(models.Model):
    """
    A model to hold vehicle history data, we are going to use 
    location, distance and fuel consumed to obtain fuel efficiency (km/lt)
    """
    vehicle = models.ForeignKey(Vehicle,
                                verbose_name='Vehicle',
                                on_delete=models.CASCADE)
    city_a = 0
    city_b = 1
    city_c = 2
    location_options = ((city_a, 'Desconocido'),
                        (city_b, 'Bajo'),
                        (city_c, 'Regular'),)
    current_location = models.IntegerField(choices=location_options,
                                           default=city_a,
                                           verbose_name='Current location')
    distance_traveled = models.IntegerField(verbose_name='Distance Traveled',)
    fuel_consumed = models.IntegerField(verbose_name='Fuel Consumed',)

    def __str__(self):
        return str(self.pk)
