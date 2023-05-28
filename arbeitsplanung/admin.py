from django.contrib import admin
from .models import Mitarbeiter, Arbeitsplan, Schicht
from django.utils.html import format_html

class MitarbeiterAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_name', 'telefonnummer', 'verfuegbarkeit', 'display_foto', 'arbeitsstunden')

    def get_name(self, obj):
        return obj.name  # Replace 'obj.full_name' with the correct attribute or field name
    get_name.short_description = 'Name'

    def display_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="250" height="250" />', obj.foto.url)
        else:
            return "No Image"
    display_foto.short_description = 'Foto'

class SchichtInline(admin.TabularInline):
    model = Schicht

class ArbeitsplanAdmin(admin.ModelAdmin):
    list_display = ('start_datum', 'end_datum', 'mitarbeiter', 'kunde')
    inlines = [SchichtInline]

admin.site.register(Mitarbeiter, MitarbeiterAdmin)
admin.site.register(Arbeitsplan, ArbeitsplanAdmin)
