from django.db import models
from django.db.models import Sum


class Kunden(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    adresse = models.CharField(max_length=200, blank=False, null=False)
    telefonnummer = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=True, null=True)
    stundenansatz = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)

    def gesamtstunden_pro_monat(self):
        from zeiterfassung.models import Zeiteintrag
        gesamtstunden = Zeiteintrag.objects.filter(kunde=self).aggregate(total=Sum(models.F('endzeit') - models.F('startzeit')))['total']
        return gesamtstunden

    def __str__(self):
        return self.name


class Zeiteintrag(models.Model):
    mitarbeiter_name = models.CharField(max_length=200, blank=False, null=False)
    kunde = models.ForeignKey(Kunden, on_delete=models.CASCADE, related_name='zeiteintraege')
    startzeit = models.DateTimeField()
    endzeit = models.DateTimeField()

    def berechne_stunden(self):
        stunden_delta = self.endzeit - self.startzeit
        return stunden_delta.total_seconds() / 3600

    def save(self, *args, **kwargs):
        self.stunden = self.berechne_stunden()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.mitarbeiter_name} - {self.kunde.name} - {self.startzeit} bis {self.endzeit}"
