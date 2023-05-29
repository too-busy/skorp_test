from django.contrib import admin
from .models import Kunden

class KundenAdmin(admin.ModelAdmin):
    list_display = ('name', 'adresse', 'telefonnummer', 'email', 'nfctag_count','gesamtstunden_pro_monat_anzeigen', 'gesamtstunden_allgemein_anzeigen'  )

    def gesamtstunden_allgemein_anzeigen(self, obj):
        gesamtstunden = obj.gesamtstunden()
        if gesamtstunden is not None:
            hours = gesamtstunden // 3600
            minutes = (gesamtstunden % 3600) // 60
            return f"{hours} Stunden {minutes} Minuten"
        else:
            return 'Keine Gesamtstunden vorhanden'
    gesamtstunden_allgemein_anzeigen.short_description = 'Gesamtstunden'

    def gesamtstunden_pro_monat_anzeigen(self, obj):
        gesamtstunden = obj.gesamtstunden_pro_monat()
        if gesamtstunden is not None:
            hours = gesamtstunden // 3600
            minutes = (gesamtstunden % 3600) // 60
            return f"{hours} Stunden {minutes} Minuten"
        else:
            return 'Keine Gesamtstunden diesen Monat vorhanden'
    gesamtstunden_pro_monat_anzeigen.short_description = 'Gesamtstunden diesen Monat'


admin.site.register(Kunden, KundenAdmin)
