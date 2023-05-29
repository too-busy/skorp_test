from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear
from datetime import datetime
from django.db import models
from django.db.models import Count

class Kunden(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    adresse = models.CharField(max_length=200, blank=False, null=False)
    telefonnummer = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=True, null=True)
    stundenansatz = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)

    @property
    def nfctag_count(self):
        return self.nfctags.count()

    def gesamtstunden(self):
        from zeiterfassung.models import Zeiteintrag
        gesamtstunden = \
        Zeiteintrag.objects.filter(kunde=self).aggregate(total=Sum(models.F('endzeit') - models.F('startzeit')))[
            'total']
        return gesamtstunden.total_seconds() if gesamtstunden else None

    def gesamtstunden_pro_monat(self):
        from zeiterfassung.models import Zeiteintrag
        current_month = datetime.now().month
        gesamtstunden = Zeiteintrag.objects.filter(kunde=self, startzeit__month=current_month).aggregate(
            total=Sum(models.F('endzeit') - models.F('startzeit')))['total']
        return gesamtstunden.total_seconds() if gesamtstunden else None
    def __str__(self):
        return self.name

class Zeiteintrag(models.Model):
    mitarbeiter_name = models.CharField(max_length=200, blank=False, null=False)
    kunde = models.ForeignKey(Kunden, on_delete=models.CASCADE, related_name='zeiteintraege')
    startzeit = models.DateTimeField()
    endzeit = models.DateTimeField()

    def berechne_stunden(self):
        stunden_delta = self.endzeit - self.startzeit
        return (stunden_delta.days * 24) + (stunden_delta.seconds // 3600)

    def save(self, *args, **kwargs):
        self.stunden = self.berechne_stunden()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.mitarbeiter_name} - {self.kunde.name} - {self.startzeit} bis {self.endzeit}"
