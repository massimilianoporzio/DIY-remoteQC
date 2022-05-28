# Generated by Django 4.0.4 on 2022-05-28 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyQC', '0006_dailyqc_deltacontrast_dailyqc_deltad03_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyqc',
            name='deltaMTF10',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True),
        ),
        migrations.AddField(
            model_name='dailyqc',
            name='deltaMTF20',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True),
        ),
    ]