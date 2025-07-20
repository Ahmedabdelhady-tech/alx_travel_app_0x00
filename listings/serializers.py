from rest_framework import serializers
from .models import Listing, Booking


class LitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fileds = "__all__"


class Bookingserializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
