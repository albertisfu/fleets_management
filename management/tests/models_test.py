import pytest
from mixer.backend.django import mixer
from management.models import Vehicle, VehicleHistory

pytestmark = pytest.mark.django_db


class TestVehicle:
    def test_model(self):
        """
        Test to check if a vehicle instance is properly created.
        """
        vehicle = mixer.blend(Vehicle)
        assert vehicle.pk == 1, 'Create a Vehicle instance'


class TestVehicleHistory:
    def test_model(self):
        """
        Test to check if a vehicle history instance is properly created.
        """
        vehicle = mixer.blend(Vehicle)
        city_a = 1
        history_vehicle = mixer.blend(VehicleHistory, vehicle=vehicle,
                                      current_location=city_a,
                                      distance_traveled=2, fuel_consumed=10)

        assert history_vehicle.vehicle.pk == 1, 'Check Vehicle relation'

        assert history_vehicle.current_location == 1 \
            and history_vehicle.distance_traveled == 2 \
            and history_vehicle.fuel_consumed == 10, \
            'Check History Vehicle Instance'
