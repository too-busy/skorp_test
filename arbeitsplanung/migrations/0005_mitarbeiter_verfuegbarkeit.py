# Generated by Django 4.2.1 on 2023-05-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbeitsplanung', '0004_alter_mitarbeiter_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='mitarbeiter',
            name='verfuegbarkeit',
            field=models.CharField(choices=[('frei', 'Frei'), ('on work', 'On Work'), ('ferien', 'Ferien'), ('krank', 'Krank')], default='frei', max_length=10),
        ),
    ]