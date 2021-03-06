import pytest
from mixer.backend.django import mixer
from management.models import Vehicle, VehicleHistory

pytestmark = pytest.mark.django_db


@pytest.fixture
def vehicle(db) -> Vehicle:
    vehicle = mixer.blend(Vehicle, vehicle_id=1)
    mixer.blend(VehicleHistory, vehicle=vehicle,
                current_location='city_a')
    mixer.blend(VehicleHistory, vehicle=vehicle,
                current_location='city_b')
    mixer.blend(VehicleHistory, vehicle=vehicle,
                current_location='city_c')
    return vehicle


@pytest.fixture
def empty_vehicle(db) -> Vehicle:
    vehicle = mixer.blend(Vehicle, vehicle_id=1)
    return vehicle


class TestVehicle:
    def test_model(self, empty_vehicle: Vehicle):
        """
        Test to check if a vehicle instance is properly created.
        """
        assert empty_vehicle.vehicle_id == 1, 'Create a Vehicle instance'

    def test_get_vehicle_history(self, vehicle: Vehicle,
                                 empty_vehicle: Vehicle):
        """
        Test get_vehicle_history function
        it has to match with 3 instances created in fixtures
        """
        history = vehicle.get_vehicle_history
        assert history.count() == 3, 'Check if it returns 3 instances created'

        history = empty_vehicle.get_vehicle_history
        assert history.count() == 0, 'Check if it returns'

    def test_current_location(self, vehicle: Vehicle,
                              empty_vehicle: Vehicle):
        current_location = vehicle.current_location
        assert current_location == 'city_c', \
            'Check if current location match with latest history created'

        current_location = empty_vehicle.current_location
        assert current_location == 'no_travel_yet', \
            'Check if current location is blank if vehicle does not have trips'

    def test_last_trip_distance(self, vehicle: Vehicle,
                                empty_vehicle: Vehicle):
        """
        Test last_trip_distance function, it has to return last trip
        distance of a vehicle
        """
        last_distance = vehicle.last_trip_distance
        assert last_distance == 4, \
            'Check if last distance match with last trip'

        last_distance = empty_vehicle.last_trip_distance
        assert last_distance == 0, \
            'Check if last distance is 0 if vehicle does not have trips'

    def test_total_distance(self, vehicle: Vehicle,
                            empty_vehicle: Vehicle):
        """
        Test test_total_distance function, it has to return total
        distance from a vehicle from history travel
        """

        total_distance = vehicle.total_distance
        assert total_distance == 5, \
            'Check if total distance match'

        total_distance = empty_vehicle.total_distance
        assert total_distance == 0, \
            'Check if total distance is 0 if vehicle does not have trips'

    def test_fuel_efficency(self, vehicle: Vehicle,
                            empty_vehicle: Vehicle):
        """
        Test fuel_efficency it has to return trip fuel effiency km/lt
        """
        fuel_efficency = vehicle.fuel_efficency
        assert fuel_efficency == 10, \
            'Check if fuel effiency match'

        fuel_efficency = empty_vehicle.fuel_efficency
        assert fuel_efficency == 0, \
            'Check if fuel effiency is 0 if vehicle does not have trips'

    def test_fuel_total_efficency(self, vehicle: Vehicle,
                                  empty_vehicle: Vehicle):
        """
        Test fuel_efficency it has to return total fuel effiency km/lt
        """
        fuel_efficency = vehicle.fuel_total_efficency
        assert float(fuel_efficency) == 10, \
            'Check if fuel effiency match'

        fuel_efficency = empty_vehicle.fuel_total_efficency
        assert fuel_efficency == 0, \
            'Check if fuel effiency is 0 if vehicle does not have trips'


class TestVehicleHistory:
    def test_model(self):
        """
        Test to check if a vehicle history instance is properly created.
        """
        vehicle = mixer.blend(Vehicle, vehicle_id=1)
        history_vehicle = mixer.blend(VehicleHistory, vehicle=vehicle,
                                      current_location='city_a')

        assert history_vehicle.vehicle.vehicle_id == 1, 'Check Vehicle relation'

        assert history_vehicle.current_location == 'city_a' \
            and history_vehicle.distance_traveled == 0 \
            and history_vehicle.fuel_consumed == 0, \
            'Check History Vehicle Instance'
