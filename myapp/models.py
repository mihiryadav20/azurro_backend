from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Turf(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    price_per_hour_least = models.IntegerField()
    price_per_hour_max = models.IntegerField(default=0)
    available_hours = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        avg_rating = self.average_rating()
        return f"{self.name}, {self.location} - Average Rating: {avg_rating:.1f}" if avg_rating is not None else f"{self.name}, {self.location} - No ratings yet"

    def average_rating(self):
        total_ratings = sum(review.rating for review in self.reviews.all())
        num_reviews = self.reviews.count()
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return None

class Review(models.Model):
    turf = models.ForeignKey(Turf, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Rating {self.rating} for {self.turf.name} by {self.user.first_name}"

class Booking(models.Model):
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Booking for {self.turf.name} by {self.user.first_name} from {self.start_time} to {self.end_time}"