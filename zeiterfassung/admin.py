from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .models import Zeiteintrag

class MonthFilter(admin.SimpleListFilter):
    title = _('Monat')
    parameter_name = 'month'

    def lookups(self, request, model_admin):
        return [
            (1, _('Januar')),
            (2, _('Februar')),
            (3, _('März')),
            (4, _('April')),
            (5, _('Mai')),
            (6, _('Juni')),
            (7, _('Juli')),
            (8, _('August')),
            (9, _('September')),
            (10, _('Oktober')),
            (11, _('November')),
            (12, _('Dezember')),
        ]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(startzeit__month=self.value())

class ZeiteintragAdmin(admin.ModelAdmin):
    list_display = ('mitarbeiter', 'kunde', 'startzeit', 'endzeit', 'arbeitsstunden')
    list_filter = (MonthFilter, 'kunde')

    def arbeitsstunden(self, obj):
        return (obj.endzeit - obj.startzeit).total_seconds() / 3600

    def get_month(self, obj):
        return obj.startzeit.strftime('%B')

    get_month.short_description = 'Monat'
    get_month.admin_order_field = 'startzeit'

admin.site.register(Zeiteintrag, ZeiteintragAdmin)
