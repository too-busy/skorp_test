from django.db import models
from django.core.validators import MinValueValidator
from kundendatenbank.models import Kunden
from datetime import datetime, timedelta
from django.db.models import Sum

class Rechnung(models.Model):
    kunde = models.ForeignKey(Kunden, on_delete=models.CASCADE)
    erstellt_am = models.DateField(auto_now_add=True)
    gesamtsumme = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    monat = models.IntegerField()  # Add the 'monat' field

    def berechne_gesamtsumme(self):
        erster_tag_des_monats = datetime(self.erstellt_am.year, self.monat, 1)
        erster_tag_des_naechsten_monats = erster_tag_des_monats + timedelta(days=32)
        zeiteintraege = self.kunde.zeiterfassung_zeiteintraege.filter(
            startzeit__gte=erster_tag_des_monats,
            startzeit__lt=erster_tag_des_naechsten_monats
        )
        gesamtstunden = zeiteintraege.aggregate(total_stunden=Sum(models.F('stunden')))['total_stunden']
        if gesamtstunden is not None:
            gesamtsumme = gesamtstunden * self.kunde.stundenansatz
            return gesamtsumme
        return 0.00

    def save(self, *args, **kwargs):
        if not self.erstellt_am:
            self.erstellt_am = datetime.now().date()  # Set the current date if erstellt_am is not set
        self.gesamtsumme = self.berechne_gesamtsumme()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Rechnung für {self.kunde.name} am {self.erstellt_am}"
