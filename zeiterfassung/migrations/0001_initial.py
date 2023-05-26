# Generated by Django 4.2.1 on 2023-05-26 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kundendatenbank', '0002_rename_kunde_kunden'),
        ('arbeitsplanung', '0005_mitarbeiter_verfuegbarkeit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zeiteintrag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startzeit', models.DateTimeField()),
                ('endzeit', models.DateTimeField()),
                ('kunde', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kundendatenbank.kunden')),
                ('mitarbeiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arbeitsplanung.mitarbeiter')),
            ],
        ),
    ]
