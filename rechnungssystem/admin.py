from django import forms
from django.contrib import admin
from .models import Rechnung

class RechnungAdminForm(forms.ModelForm):
    class Meta:
        model = Rechnung
        fields = ['kunde', 'monat']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['kunde'].queryset = self.fields['kunde'].queryset.only('name')
        self.fields['monat'].widget = forms.Select(choices=self.get_month_choices())

    def get_month_choices(self):
        month_choices = []
        for i in range(1, 13):
            month_choices.append((i, forms.DateField().to_python(f'2023-{i:02d}-01').strftime('%B')))
        return month_choices

class RechnungAdmin(admin.ModelAdmin):
    form = RechnungAdminForm
    list_display = ('kunde', 'get_monat_name', 'gesamtsumme')

    def get_monat_name(self, obj):
        return self.get_month_name(obj.monat)

    def get_month_name(self, month):
        months = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
        return months[month - 1]

    get_monat_name.short_description = 'Monat'

admin.site.register(Rechnung, RechnungAdmin)
