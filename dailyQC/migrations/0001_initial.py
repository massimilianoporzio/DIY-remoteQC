# Generated by Django 4.0.4 on 2022-04-23 20:29

import dailyQC.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyQC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=dailyQC.models.default_datetime, null=True)),
                ('datetimeJava', models.DateTimeField(blank=True, default=dailyQC.models.default_datetime, null=True)),
                ('SIGNAL', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('SNR', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('SDNR', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('MTF50', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('MTF20', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('MTF10', models.DecimalField(decimal_places=3, default=0, max_digits=5)),
                ('D03', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('D4', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('mAs', models.DecimalField(decimal_places=3, default=0, max_digits=7)),
                ('baseline', models.BooleanField(blank=True, default=False)),
            ],
        ),
    ]
