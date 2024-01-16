from django.contrib import admin
from .models import Event, Images


class ImagesInline(admin.TabularInline):
    model = Images


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]


admin.site.register(Images)
