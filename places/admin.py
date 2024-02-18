from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminBase

from .models import Event, Image


class ImagesInline(SortableStackedInline, admin.TabularInline):
    model = Image

    readonly_fields = ["get_preview"]

    def get_preview(self, obj):
        width = obj.img.width
        height = obj.img.height
        max_height = 200
        if height > max_height:
            width = width*(max_height/height)
            height = max_height
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.img.url,
            width=width,
            height=height,
            )
        )


@admin.register(Event)
class EventAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]


admin.site.register(Image)
