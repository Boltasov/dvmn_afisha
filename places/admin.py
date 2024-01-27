from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline, SortableAdminMixin, SortableAdminBase

from .models import Event, Image


class ImagesInline(SortableStackedInline, admin.TabularInline):
    model = Image

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
class EventAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImagesInline,
    ]


admin.site.register(Image)
