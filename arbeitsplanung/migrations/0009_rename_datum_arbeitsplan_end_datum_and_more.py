from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kundendatenbank', '0005_remove_zeiteintrag_mitarbeiter_and_more'),
        ('arbeitsplanung', '0008_arbeitsplan_schichten'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arbeitsplan',
            old_name='datum',
            new_name='end_datum',
        ),
        migrations.RemoveField(
            model_name='arbeitsplan',
            name='mitarbeiter',
        ),
        migrations.RemoveField(
            model_name='arbeitsplan',
            name='schichten',
        ),
        migrations.AddField(
            model_name='arbeitsplan',
            name='kunde',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='kundendatenbank.kunden'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arbeitsplan',
            name='mitarbeiter_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='arbeitsplan',
            name='start_datum',
            field=models.DateField(default='2023-01-01'),
            preserve_default=False,
        ),
    ]
