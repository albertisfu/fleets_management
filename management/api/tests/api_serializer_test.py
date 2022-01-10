import pytest
from mixer.backend.django import mixer
from management.models import Vehicle
from management.api.serializers import VehicleSerializer, \
     VehicleHistorySerializer

pytestmark = pytest.mark.django_db


@pytest.fixture
def empty_vehicle(db) -> Vehicle:
    vehicle = mixer.blend(Vehicle, fuel_level='150.00')
    return vehicle


class TestVehicleSerializer:
    def test_serialize_model(self, empty_vehicle: Vehicle):
        """
        Test to check if model to data serializer works properly
        """
        serializer = VehicleSerializer(empty_vehicle)
        assert serializer.data

    def test_deserializer(self):
        """
        Test to check data to model deserialization works properly
        """

        test_json = {
            'vehicle_id': 2,
            'fuel_level': '100.00',
        }

        serializer = VehicleSerializer(data=test_json)

        assert serializer.is_valid()
        assert serializer.errors == {}


class TestVehicleHistorySerializer:
    def test_deserializer(self):
        """
        Test to check deserialization works properly
        """
        location = 'city_a'
        test_json = {
            'current_location': location,
        }

        serializer = VehicleHistorySerializer(data=test_json)

        assert serializer.is_valid()
        assert serializer.errors == {}
