from django.urls import include, path
from management.api.views import VehicleViewSet, send_instruction
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    # Rest framework include
    path('', include('rest_framework.urls', namespace='rest_framework')),
    # Get token endpoint
    path('get_auth_token', obtain_auth_token, name='get_auth_token'),

    # list and create Vehicles endpoint
    path('vehicles', VehicleViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='vehicle_url'),

    # retrieve, update and destroy Vehicles endpoint
    path('vehicles/<str:pk>', VehicleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='vehicle_url_id'),

    path('send_instruction/<int:pk>', send_instruction,
         name='instruction_url'),

    ]
