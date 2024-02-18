from django.db import models
from tinymce.models import HTMLField


class Event(models.Model):
    title = models.CharField(
        max_length=500,
        verbose_name="Заголовок"
    )
    description_short = models.TextField(verbose_name="Короткое описание")
    description_long = HTMLField(verbose_name="Длинное описание")
    coordinates_lng = models.DecimalField(
        max_digits=20,
        decimal_places=15,
        verbose_name="Долгота"
    )
    coordinates_lat = models.DecimalField(
        max_digits=20,
        decimal_places=15,
        verbose_name="Широта"
    )

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return self.title


class Image(models.Model):
    order = models.IntegerField(
        default=0,
        blank=False,
        null=False,
        verbose_name="Порядок")

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name="Событие")
    img = models.ImageField(verbose_name="Изображение")

    class Meta:
        ordering = ['order']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f'{self.order} {self.event}'
