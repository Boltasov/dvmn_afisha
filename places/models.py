from django.db import models
from tinymce.models import HTMLField


class Event(models.Model):
    title = models.CharField(
        max_length=500,
        unique=True,
        verbose_name="Заголовок"
    )
    short_description = models.TextField(
        verbose_name="Короткое описание",
        blank=True,
    )
    long_description = HTMLField(
        verbose_name="Длинное описание",
        blank=True,
    )
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
        db_index=True,
        blank=False,
        null=False,
        verbose_name="Порядок")

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name="Событие",
        related_name="images")
    img = models.ImageField(verbose_name="Изображение")

    class Meta:
        ordering = ['order']
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f'{self.order} {self.event}'
