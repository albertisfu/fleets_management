import pytest
from mixer.backend.django import mixer
from management.models import Vehicle, VehicleHistory

pytestmark = pytest.mark.django_db


@pytest.fixture
def instance_vehicle(db) -> Vehicle:
    city_a = 0
    city_b = 1
    city_c = 2
    vehicle = mixer.blend(Vehicle)
    mixer.blend(VehicleHistory, vehicle=vehicle,
                current_location=city_a,
                distance_traveled=0, fuel_consumed=0)
    mixer.blend(VehicleHistory, vehicle=vehicle,
                current_location=city_b,
                distance_traveled=20, fuel_consumed=10)
    mixer.blend(VehicleHistory, vehicle=vehicle,
                current_location=city_c,
                distance_traveled=30, fuel_consumed=25)
    return vehicle


class TestVehicle:
    def test_model(self):
        """
        Test to check if a vehicle instance is properly created.
        """
        vehicle = mixer.blend(Vehicle)
        assert vehicle.pk == 1, 'Create a Vehicle instance'

    def test_get_vehicle_travel_history(self, instance_vehicle: Vehicle):
        """
        Test get_vehicle_travel_history function,
        it has to match with 3 instances created in fixtures
        """
        history = instance_vehicle.get_vehicle_travel_history()
        # print('history cities', history)
        # print('history cities', [x.current_location for x in history])
        assert history.count() == 3, 'Check if it return 3 instances created'

    def test_get_current_location(self, instance_vehicle: Vehicle):
        current_location = instance_vehicle.get_current_location()
        assert current_location == 'city_c', \
            'Check if current location match with latest history created'


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
