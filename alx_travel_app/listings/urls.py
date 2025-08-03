from django.urls import path, include
from .views import ListingViewSet, BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"listings", ListingViewSet, basename="listing")
router.register(r"booking", BookingViewSet, basename="booking")

urlpatterns = [
    path("", include(router.urls)),
]
