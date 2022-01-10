from django.db import models
# Create your models here.
from django.db.models import Sum
import decimal


class Vehicle(models.Model):
    """
    A model to hold vehicle information.
    """
    vehicle_id = models.IntegerField(verbose_name='Vehicle ID',)
    add_date = models.DateTimeField(verbose_name='Creation Date',
                                    auto_now_add=True)

    @property
    def get_vehicle_history(self):
        """
        Get Vechicle Travel History
        :return: <QuerySet [<VehicleHistory: 1>, <VehicleHistory: 2>]>
        """
        history_travel = self.vehiclehistory_set.all().order_by('-add_date')
        return history_travel

    @property
    def current_location(self):
        """
        Get current vehicle location,
        latest vehicle history instance register for vehicle
        :return: city_x
        """
        history_travel = self.vehiclehistory_set.all().order_by('-add_date')
        if history_travel.count() > 0:
            return history_travel[0].get_current_location_display()
        else:
            return 'no_travel_yet'

    @property
    def last_trip_distance(self):
        """
        Get last vehicle trip distance,
        :return: decimal (distance)
        """
        history_travel = self.vehiclehistory_set.all().order_by('-add_date')
        if history_travel.count() > 0:
            return history_travel[0].distance_traveled
        else:
            return 0

    @property
    def total_distance(self):
        """
        Get total vehicle distance,
        :return: decimal (distance)
        """
        history_travel = self.vehiclehistory_set.all()
        if history_travel.count() > 0:
            total_distance = history_travel.aggregate(Sum('distance_traveled'))
            return total_distance['distance_traveled__sum']
        else:
            return 0

    @property
    def fuel_efficency(self):
        """
        Get last trip fuel efficency,
        :return: decimal (fuel effiency, km/lt)
        """
        history_travel = self.vehiclehistory_set.all().order_by('-add_date')
        if history_travel.count() > 0:
            distance = history_travel[0].distance_traveled
            fuel_consumed = history_travel[0].fuel_consumed

            # handle zero division
            try:
                fuel_effiency = distance/fuel_consumed
            except decimal.InvalidOperation:
                fuel_effiency = 0
            return fuel_effiency
        else:
            return 0

    @property
    def fuel_total_efficency(self):
        """
        Get total vehicle fuel efficency,
        :return: decimal (fuel effiency, km/lt)
        """
        total_distance = self.total_distance
        history_travel = self.vehiclehistory_set.all()
        if history_travel.count() > 0:
            total_fuel = history_travel.aggregate(Sum('fuel_consumed'))
            fuel_consumed = total_fuel['fuel_consumed__sum']
            try:
                total_fuel_effiency = round(total_distance / fuel_consumed, 2)
            except decimal.InvalidOperation:
                total_fuel_effiency = 0

            return total_fuel_effiency
        else:
            return 0

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
    location_options = (('city_a', 'city_a'),
                        ('city_b', 'city_b'),
                        ('city_c', 'city_c'),)
    current_location = models.CharField(max_length=20,
                                        choices=location_options,
                                        default='city_a',
                                        verbose_name='Current location')
    distance_traveled = models.DecimalField(verbose_name='Travel Distance KM',
                                            decimal_places=4, max_digits=6,
                                            default=0)
    fuel_consumed = models.DecimalField(verbose_name='Fuel Consumed LT',
                                        decimal_places=4, max_digits=6,
                                        default=0)
    add_date = models.DateTimeField(verbose_name='Creation Date',
                                    auto_now_add=True)

    def save(self, *args, **kwargs):
        """
        Override save method to calculate distance based on provided data
        fuel effiency to calculate fuel consumed is a constant
        """

        # asign distance from cities:
        distances = {
            'city_a': {'city_a': 0, 'city_b': 1, 'city_c': 2},
            'city_b': {'city_a': 1, 'city_b': 0, 'city_c': 4},
            'city_c': {'city_a': 2, 'city_b': 4, 'city_c': 0},
            }

        # fuel effiency km/l
        fuel_effiency = 10

        objects = VehicleHistory.objects.filter(vehicle=self.vehicle).count()
        if objects == 0:
            self.distance_traveled = 0
            self.fuel_consumed = 0
        else:
            # get previous location
            origin = self.vehicle.current_location
            destine = self.current_location
            distance = distances[origin][destine]
            self.distance_traveled = distance
            self.fuel_consumed = distance/fuel_effiency

        super(VehicleHistory, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)
