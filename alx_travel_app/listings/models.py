from django.db import models


class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    listing = models.ForeignKey(
        Listing, related_name="bookings", on_delete=models.CASCADE
    )
    guest_name = models.CharField(max_length=255)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Booking by {self.guest_name} for {self.listing.title}"


class Review(models.Model):
    listing = models.ForeignKey(
        Listing, related_name="reviews", on_delete=models.CASCADE
    )
    reviewer_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.reviewer_name} for {self.listing.title}"
