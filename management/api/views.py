from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from management.models import Vehicle, VehicleHistory
from management.api.serializers import VehicleSerializer, \
     VehicleHistorySerializer, VehicleCustomSerializer


class VehicleViewSet(viewsets.ViewSet):
    """
    Vehicle Viewset with list, create, retrieve, update and destroy endpoints
    """
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleCustomSerializer(vehicles, many=True)
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


@permission_classes((IsAuthenticated,))
@api_view(['PUT'])
def send_instruction(request, pk):
    """
    send_instruction endpoint, tell a vehicle :pk where to travel
    inside body request 'current_location': city_x
    """
    if request.method == 'PUT':
        try:
            vehicle = Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VehicleHistorySerializer(data=request.data)
        if serializer.is_valid():
            current_location = serializer.data["current_location"]
            VehicleHistory.objects.create(vehicle=vehicle,
                                          current_location=current_location)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
