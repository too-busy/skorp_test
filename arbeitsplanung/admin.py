from django.contrib import admin
from .models import Mitarbeiter, Arbeitsplan, Schicht
from django.utils.html import format_html

class MitarbeiterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'telefonnummer', 'verfuegbarkeit', 'display_foto', 'arbeitsstunden')

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




admin.site.register(Mitarbeiter, MitarbeiterAdmin)
admin.site.register(Arbeitsplan, ArbeitsplanAdmin)
