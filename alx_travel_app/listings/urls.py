from django.urls import path
from .views import ListingListCreateAPIView

urlpatterns = [
    path("", ListingListCreateAPIView.as_view(), name="listings"),
]
