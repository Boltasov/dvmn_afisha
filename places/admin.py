from django.contrib import admin
from django.utils.html import format_html

from .models import Event, Images


class ImagesInline(admin.TabularInline):
    model = Images

    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        width = obj.img.width
        height = obj.img.height
        if height > 200:
            width = width*(200/height)
            height = 200
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.img.url,
            width=width,
            height=height,
            )
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]


admin.site.register(Images)
