from django.db import models
from django.utils import timezone
# Create your models here.


def default_datetime():
    now = timezone.now()
    default = now.replace(microsecond=0)
    return default


class DailyQC(models.Model):
    date = models.DateField(null=True, default=default_datetime, blank=True)  # quando hanno fatto il cq sulla macchina
    datetimeJava = models.DateTimeField(null=True, default=default_datetime,
                                        blank=True)  # quando è stato eseguito lato java l'analisi

    SIGNAL = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False, default=0)
    SNR = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False, default=0)
    SDNR = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=False, default=0)

    MTF50 = models.DecimalField(max_digits=5, decimal_places=3, blank=False, null=False, default=0)
    MTF20 = models.DecimalField(max_digits=5, decimal_places=3, blank=False, null=False, default=0)
    MTF10 = models.DecimalField(max_digits=5, decimal_places=3, blank=False, null=False, default=0)

    #d'
    D03 = models.DecimalField(max_digits=6, decimal_places=3, blank=False, null=False, default=0)
    D4 = models.DecimalField(max_digits=6, decimal_places=3, blank=False, null=False, default=0)

    mAs = models.DecimalField(max_digits=7, decimal_places=3, blank=False, null=False, default=0)

    baseline = models.BooleanField(blank=True,null=False, default=False)