from django.db import models
from kundendatenbank.models import Kunden
from datetime import timedelta

class Zeiteintrag(models.Model):
    mitarbeiter = models.ForeignKey('arbeitsplanung.Mitarbeiter', on_delete=models.CASCADE, related_name='zeiteintraege')
    kunde = models.ForeignKey(Kunden, on_delete=models.CASCADE, related_name='zeiterfassung_zeiteintraege')
    startzeit = models.DateTimeField()
    endzeit = models.DateTimeField()
    stunden = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.berechne_stunden()
        super().save(*args, **kwargs)

    def berechne_stunden(self):
        if self.startzeit and self.endzeit:
            stunden_delta = self.endzeit - self.startzeit
            self.stunden = stunden_delta.total_seconds() / 3600
        else:
            self.stunden = None

    def __str__(self):
        return f"{self.mitarbeiter.name} - {self.kunde.name} - {self.startzeit} bis {self.endzeit}"
