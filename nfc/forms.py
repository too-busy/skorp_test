from django import forms
from .models import NfcScan

class NfcScanForm(forms.ModelForm):
    class Meta:
        model = NfcScan
        fields = ['image', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),  # Anpassen der Darstellung des Textareas
        }
