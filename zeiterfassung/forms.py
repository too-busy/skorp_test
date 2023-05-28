from django import forms
from .models import Zeiteintrag
from arbeitsplanung.models import Mitarbeiter

class ZeiteintragForm(forms.ModelForm):
    startzeit = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'], widget=forms.TextInput(attrs={'class': 'datetimepicker'}))
    endzeit = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M'], widget=forms.TextInput(attrs={'class': 'datetimepicker'}))

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
        self.fields['mitarbeiter'].required = True

    def clean(self):
        cleaned_data = super().clean()
        startzeit = cleaned_data.get('startzeit')
        endzeit = cleaned_data.get('endzeit')

        if startzeit and endzeit and endzeit < startzeit:
            self.add_error('endzeit', 'Die Endzeit darf nicht vor der Startzeit liegen.')

        return cleaned_data
