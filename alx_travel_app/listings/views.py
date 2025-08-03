from django.shortcuts import render
from .models import Listing, Booking
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .serializers import ListingSerializer, BookingSerializer


class ListingListCreateAPIView(ListCreateAPIView):
    def list(self, request, *args, **kwargs):
        return Response({"detail": "This is your listings endpoint"})

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Create a listing"})


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
