# Generated by Django 4.2.1 on 2023-05-26 15:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kundendatenbank', '0002_rename_kunde_kunden'),
        ('rechnungssystem', '0002_remove_rechnung_kunde_rechnung_mitarbeiter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rechnung',
            name='mitarbeiter',
        ),
        migrations.AddField(
            model_name='rechnung',
            name='kunde',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='kundendatenbank.kunden'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rechnung',
            name='gesamtsumme',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
