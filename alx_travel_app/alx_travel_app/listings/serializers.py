from .models import Listing, Booking, Review
from rest_framework import serializers

class ListingSerializer(serializers.ModelSerializer):
    """ Serializer for the Listing model. """

    class Meta:
        model = Listing
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    """ Serializer for the Booking model. """

    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    """ Serializer for the Review model. """

    class Meta:
        model = Review
        fields = '__all__'
