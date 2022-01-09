from rest_framework import serializers
from management.models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    """
    VehicleModel Serializer with all Fields
    """
    class Meta:
        model = Vehicle
        fields = '__all__'
