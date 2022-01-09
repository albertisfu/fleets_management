import pytest
from mixer.backend.django import mixer
from management.models import Vehicle, VehicleHistory

pytestmark = pytest.mark.django_db


@pytest.fixture
def vehicle(db) -> Vehicle:
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


@pytest.fixture
def empty_vehicle(db) -> Vehicle:
    vehicle = mixer.blend(Vehicle)
    return vehicle


class TestVehicle:
    def test_model(self, empty_vehicle: Vehicle):
        """
        Test to check if a vehicle instance is properly created.
        """
        assert empty_vehicle.pk == 1, 'Create a Vehicle instance'

    def test_get_vehicle_history(self, vehicle: Vehicle,
                                 empty_vehicle: Vehicle):
        """
        Test get_vehicle_history function
        it has to match with 3 instances created in fixtures
        """
        history = vehicle.get_vehicle_history()
        assert history.count() == 3, 'Check if it returns 3 instances created'

        history = empty_vehicle.get_vehicle_history()
        assert history.count() == 0, 'Check if it returns'

    def test_get_current_location(self, vehicle: Vehicle,
                                  empty_vehicle: Vehicle):
        current_location = vehicle.get_current_location()
        assert current_location == 'city_c', \
            'Check if current location match with latest history created'

        current_location = empty_vehicle.get_current_location()
        assert current_location == '', \
            'Check if current location is blank if vehicle does not have trips'

    def test_get_last_trip_distance(self, vehicle: Vehicle,
                                    empty_vehicle: Vehicle):
        """
        Test get_last_trip_distance function, it has to return last trip
        distance of a vehicle
        """
        last_distance = vehicle.get_last_trip_distance()
        assert last_distance == 30, \
            'Check if last distance match with last trip'

        last_distance = empty_vehicle.get_last_trip_distance()
        assert last_distance == 0, \
            'Check if last distance is 0 if vehicle does not have trips'


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
