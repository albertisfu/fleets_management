from django.db import models
# Create your models here.


class Vehicle(models.Model):
    """
    A model to hold vehicle information.
    """
    vehicle_id = models.IntegerField(verbose_name='Vehicle ID',)
    fuel_level = models.DecimalField(verbose_name='Fuel Level', max_digits=6,
                                     decimal_places=2, default=0)
    add_date = models.DateTimeField(verbose_name='Creation Date',
                                    auto_now_add=True)

    def get_vehicle_travel_history(self):
        """
        Get Vechicle Travel History
        :return: <QuerySet [<VehicleHistory: 1>, <VehicleHistory: 2>]>
        """
        history_travel = self.vehiclehistory_set.all()
        return history_travel

    def get_current_location(self):
        """
        Get current vehicle location,
        latest vehicle history instance register for vehicle
        :return: city_x
        """
        history_travel = self.vehiclehistory_set.all().order_by('-add_date')[0]
        return history_travel.get_current_location_display()

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
    location_options = ((city_a, 'city_a'),
                        (city_b, 'city_b'),
                        (city_c, 'city_c'),)
    current_location = models.IntegerField(choices=location_options,
                                           default=city_a,
                                           verbose_name='Current location')
    distance_traveled = models.DecimalField(verbose_name='Travel Distance KM',
                                            decimal_places=2, max_digits=6,  default=0)
    fuel_consumed = models.DecimalField(verbose_name='Fuel Consumed LT',
                                        decimal_places=2, max_digits=6, default=0)
    add_date = models.DateTimeField(verbose_name='Creation Date',
                                    auto_now_add=True)

    def __str__(self):
        return str(self.pk)
