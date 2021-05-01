from django.db import models

# Create your models here.
# crypto model
class Spot(models.Model):
    title = models.CharField(max_length=300)
    location = models.CharField(max_length=250)
    overview = models.TextField(max_length=500)
    longitude = models.FloatField(default=0)
    latitude = models.FloatField(default=0)

    def __str__(self):
        return self.title

    # redirect once a new crypto is created
    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'spot_id': self.id})