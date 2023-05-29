from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from django.utils.html import format_html
from .models import NfcTag, NfcScan

class NfcTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'kunde')

class NfcScanAdmin(admin.ModelAdmin):
    list_display = ('tag_id', 'tag', 'timestamp', 'display_kunde_name', 'user', 'display_image', 'comment')
    list_filter = (
        'tag__kunde',
        ('timestamp', DateFieldListFilter),
    )

    def tag_id(self, obj):
        return obj.tag.id
    tag_id.short_description = 'Tag ID'

    def display_kunde_name(self, obj):
        return obj.tag.kunde.name
    display_kunde_name.short_description = 'Kunde'

    def display_image(self, obj):
        if obj.image:
            return format_html('<a href="{0}" target="_blank"><img src="{0}" width="50" height="50"></a>', obj.image.url)
        else:
            return ''
    display_image.short_description = 'Bild'
    display_image.allow_tags = True

admin.site.register(NfcTag, NfcTagAdmin)
admin.site.register(NfcScan, NfcScanAdmin)
