# Generated by Django 4.2.1 on 2023-05-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zeiterfassung', '0004_remove_zeiteintrag_stunden'),
    ]

    operations = [
        migrations.AddField(
            model_name='zeiteintrag',
            name='stunden',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]
