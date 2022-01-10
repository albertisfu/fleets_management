
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse
from django.contrib.auth.models import User

import pytest
import json
from mixer.backend.django import mixer
from management.models import Vehicle

pytestmark = pytest.mark.django_db


@pytest.fixture
def empty_vehicle(db) -> Vehicle:
    vehicle = mixer.blend(Vehicle, fuel_level='100.00')
    return vehicle


@pytest.fixture
def api_client():
    """
    ApiClient fixture with valid authorization header
    """
    user = mixer.blend(User)
    token = Token.objects.create(user=user)
    token.save()
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client


class TestVehicleEndpoints:
    # get URL for endpoint base on url name
    endpoint = reverse('vehicle_url')

    def test_create(self, api_client):
        """
        Test create endpoint, pass a raw json and check if instance
        is correctly created
        """
        test_json = {
            'vehicle_id': 2,
            'fuel_level': '100.00',
        }
        response = api_client.post(
            self.endpoint,
            data=test_json,
            format='json'
        )

        json_obj = json.loads(response.content)
        assert response.status_code == 201
        assert json_obj['vehicle_id'] == test_json['vehicle_id']
        assert json_obj['fuel_level'] == test_json['fuel_level']

    def test_list(self, api_client, empty_vehicle: Vehicle):
        """
        Test list endpoint, create a vehicle and retrieve
        vehicles json list
        """
        response = api_client.get(
            self.endpoint
        )

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 1

    def test_retrieve(self, api_client, empty_vehicle: Vehicle):
        """
        Test retrieve endpoint, create a vehicle then retrieve from pk
        and check if it match
        """

        test_json = {
            'id': empty_vehicle.id,
            'vehicle_id': empty_vehicle.vehicle_id,
            'fuel_level': str(empty_vehicle.fuel_level),
        }

        url = f'{self.endpoint}/{empty_vehicle.id}'
        response = api_client.get(url)
        json_obj = json.loads(response.content)

        assert response.status_code == 200
        assert json_obj['id'] == test_json['id']
        assert json_obj['vehicle_id'] == test_json['vehicle_id']
        assert json_obj['fuel_level'] == test_json['fuel_level']

    def test_update(self, api_client, empty_vehicle: Vehicle):
        """
        Test update endpoint, create a vehicle then update its values
        and check if it match
        """

        test_json = {
            'vehicle_id': 2,
            'fuel_level': '50.00',
        }

        url = f'{self.endpoint}/{empty_vehicle.id}'

        response = api_client.put(
            url,
            test_json,
            format='json'
        )

        json_obj = json.loads(response.content)
        assert response.status_code == 202
        assert json_obj['vehicle_id'] == test_json['vehicle_id']
        assert json_obj['fuel_level'] == test_json['fuel_level']

    def test_delete(self, api_client, empty_vehicle: Vehicle):
        """
        Test delete endpoint, create a vehicle then delete,
        check if operation is performed correctly
        """

        url = f'{self.endpoint}/{empty_vehicle.id}'
        response = api_client.delete(url)
        assert response.status_code == 204
        assert Vehicle.objects.all().count() == 0


class TestInstructionEndpoint:
    """
    Test send_instruction endpoint, PUT request to
    /api/send_instruction/vehicle_pk, send travel location
    inside body request 'current_location': city_x
    """

    # get URL for endpoint based on url name
    endpoint = '/api/send_instruction'

    def test_create(self, api_client, empty_vehicle: Vehicle):
        """
        Test send instruction to vehicle endpoint,
        """
        location = 'city_a'
        test_json = {
            'current_location': location,
        }

        url = f'{self.endpoint}/{empty_vehicle.id}'
        print('url: ', url)

        response = api_client.put(
            url,
            test_json,
            format='json'
        )

        json_obj = json.loads(response.content)
        assert response.status_code == 201
        assert json_obj['current_location'] == test_json['current_location']
