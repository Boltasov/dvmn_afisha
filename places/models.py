from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=500)
    description_short = models.TextField()
    description_long = models.TextField()
    coordinates_lng = models.DecimalField(max_digits=20, decimal_places=15)
    coordinates_lat = models.DecimalField(max_digits=20, decimal_places=15)

    def __str__(self):
        return self.title


class Images(models.Model):
    order = models.IntegerField(
        default=0,
        blank=False,
        null=False,)

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    img = models.ImageField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order} {self.event}'
