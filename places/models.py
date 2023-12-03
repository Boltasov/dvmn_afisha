from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=500)
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates_lng = models.DecimalField(max_digits=20, decimal_places=15)
    coordinates_lat = models.DecimalField(max_digits=20, decimal_places=15)

    def __str__(self):
        return self.title

