from django.shortcuts import render


from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response


class ListingListCreateAPIView(ListCreateAPIView):
    def list(self, request, *args, **kwargs):
        return Response({"detail": "This is your listings endpoint"})

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Create a listing"})
