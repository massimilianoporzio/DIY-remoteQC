# Generated by Django 4.0.4 on 2022-05-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyQC', '0004_dailyqc_signal_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyqc',
            name='CONTRAST',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='dailyqc',
            name='DAP',
            field=models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='dailyqc',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyqc',
            name='esitoCONTRAST',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyqc',
            name='esitoD03',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyqc',
            name='esitoD4',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyqc',
            name='esitoMTF50',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyqc',
            name='esitoSDNR',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyqc',
            name='esitoSIGNAL',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyqc',
            name='esitoSNR',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='dailyqc',
            name='kV',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
