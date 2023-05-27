from django import forms
from django.contrib.auth import get_user_model

from .models import Zeiteintrag

User = get_user_model()

class ZeiteintragForm(forms.ModelForm):
    startzeit = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'timepicker'}))
    endzeit = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'timepicker'}))
    mitarbeiter = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Zeiteintrag
        fields = ['mitarbeiter', 'kunde', 'startzeit', 'endzeit']
        labels = {
            'mitarbeiter': 'Mitarbeiter',
            'kunde': 'Kunde',
            'startzeit': 'Startzeit',
            'endzeit': 'Endzeit',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kunde'].required = False

    def clean(self):
        cleaned_data = super().clean()
        startzeit = cleaned_data.get('startzeit')
        endzeit = cleaned_data.get('endzeit')

        if startzeit and endzeit and endzeit < startzeit:
            self.add_error('endzeit', 'Die Endzeit darf nicht vor der Startzeit liegen.')

        if startzeit:
            cleaned_data['startzeit'] = startzeit.strftime('%H:%M:%S')

        if endzeit:
            cleaned_data['endzeit'] = endzeit.strftime('%H:%M:%S')

        return cleaned_data
