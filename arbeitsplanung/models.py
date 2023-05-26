from django.db import models
from kundendatenbank.models import Kunden
from datetime import datetime, date

class Mitarbeiter(models.Model):
    VERFUEGBARKEIT_CHOICES = [
        ('frei', 'Frei'),
        ('on work', 'On Work'),
        ('ferien', 'Ferien'),
        ('krank', 'Krank'),
    ]

    name = models.CharField(max_length=200, blank=False, null=False)
    beginn_arbeitsverhaeltnis = models.DateField(blank=False, null=False)
    foto = models.ImageField(upload_to='mitarbeiter_fotos/', blank=True, null=True)
    telefonnummer = models.CharField(max_length=15, blank=False, null=False)
    stundenlohn = models.DecimalField(max_digits=5, decimal_places=2, blank=False, null=False)
    verfuegbarkeit = models.CharField(
        max_length=10,
        choices=VERFUEGBARKEIT_CHOICES,
        default='frei',
        blank=False,
        null=False
    )

    def arbeitsstunden(self):
        from zeiterfassung.models import Zeiteintrag
        zeiteintraege = Zeiteintrag.objects.filter(mitarbeiter=self)
        gesamtstunden = sum(
            (zeiteintrag.endzeit - zeiteintrag.startzeit).total_seconds() / 3600 for zeiteintrag in zeiteintraege)
        return gesamtstunden

    def __str__(self):
        return self.name


class Schicht(models.Model):
    arbeitsplan = models.ForeignKey('Arbeitsplan', on_delete=models.CASCADE)
    beginn = models.TimeField()
    ende = models.TimeField()

    def __str__(self):
        return f"{self.arbeitsplan} - {self.beginn} bis {self.ende}"



class Arbeitsplan(models.Model):
    mitarbeiter = models.ForeignKey(Mitarbeiter, on_delete=models.CASCADE)
    kunde = models.ForeignKey(Kunden, on_delete=models.CASCADE)
    start_datum = models.DateField()
    end_datum = models.DateField()

    def save(self, *args, **kwargs):
        # Convert the values to the correct date format
        if isinstance(self.start_datum, str):
            self.start_datum = date.fromisoformat(self.start_datum)
        if isinstance(self.end_datum, str):
            self.end_datum = date.fromisoformat(self.end_datum)

        super().save(*args, **kwargs)

class Zeiteintrag(models.Model):
    mitarbeiter = models.ForeignKey(Mitarbeiter, on_delete=models.CASCADE, related_name='arbeitsplanung_zeiteintraege')

    # Ihre weiteren Felder für den Zeiteintrag

    def __str__(self):
        return f"Zeiteintrag von {self.mitarbeiter.name}"