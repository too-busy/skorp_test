from django.contrib import admin
from .models import Kunden


class KundenAdmin(admin.ModelAdmin):
    list_display = ('name', 'adresse', 'telefonnummer', 'email', 'gesamtstunden_anzeigen')

    def gesamtstunden_anzeigen(self, obj):
        gesamtstunden = obj.gesamtstunden_pro_monat()
        if gesamtstunden is not None:
            hours = gesamtstunden.seconds // 3600
            minutes = (gesamtstunden.seconds % 3600) // 60
            return f"{hours} Stunden {minutes} Minuten"
        else:
            return 'Keine Gesamtstunden vorhanden'


admin.site.register(Kunden, KundenAdmin)
