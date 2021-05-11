from django.db import models

# Import the reverse function
from django.urls import reverse

# import for auth
from django.contrib.auth.models import User

# Create your models here.
# crypto model
class Spot(models.Model):
    title = models.CharField(max_length=300)
    location = models.CharField(max_length=250)
    overview = models.TextField(max_length=500)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)

    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # redirect once a new spot is created
    def get_absolute_url(self):
        return reverse('detail', kwargs={'spot_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for spot_id: {self.spot_id} @{self.url}"