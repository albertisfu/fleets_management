from rest_framework import serializers
from management.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    """
    VehicleModel Serializer with all Fields
    """
    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleCustomSerializer(serializers.ModelSerializer):
    """
    VehicleModel Serializer with all Fields
    """
    class Meta:
        model = Vehicle
        fields = 'id', 'vehicle_id', 'current_location', \
                 'last_trip_distance', 'total_distance', \
                 'fuel_efficency', 'fuel_total_efficency'


class VehicleHistorySerializer(serializers.Serializer):
    """
    VehicleModel Serializer with all Fields
    """
    current_location = serializers.CharField()
