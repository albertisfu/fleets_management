from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from management.models import Vehicle
from management.api.serializers import VehicleSerializer


class VehicleViewSet(viewsets.ViewSet):
    """
    Vehicle Viewset with list, create, retrieve, update and destroy endpoints
    """
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = VehicleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        vehicle = Vehicle.objects.get(id=pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    def update(self, request, pk=None):
        vehicle = Vehicle.objects.get(id=pk)
        serializer = VehicleSerializer(instance=vehicle, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        vehicle = Vehicle.objects.get(id=pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
