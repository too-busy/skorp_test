from django.db import models
from django.utils import timezone
from kundendatenbank.models import Kunden
from django.contrib.auth.models import User
from django.db.models import Count
from datetime import datetime


class NfcTag(models.Model):
    kunde = models.ForeignKey(Kunden, on_delete=models.CASCADE, related_name='nfctags', null=True, blank=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f'NFC Tag at {self.location}'

    @property
    def scanned_today(self):
        today = datetime.now().date()
        return self.nfcscan_set.filter(timestamp__date=today).exists()


class NfcScan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(NfcTag, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='nfc_scans/', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Scan of {self.tag} on {self.timestamp} by {self.user}'
