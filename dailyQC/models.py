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

    SIGNAL = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    deltaSIGNAL = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    SNR = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    deltaSNR = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    SDNR = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    deltaSDNR = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    CONTRAST = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    deltaCONTRAST = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)

    MTF50 = models.DecimalField(max_digits=5, decimal_places=3, blank=False, null=True, default=0)
    deltaMTF50 = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    MTF20 = models.DecimalField(max_digits=5, decimal_places=3, blank=False, null=True, default=0)
    deltaMTF20 = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    MTF10 = models.DecimalField(max_digits=5, decimal_places=3, blank=False, null=True, default=0)
    deltaMTF10 = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    #d'
    D03 = models.DecimalField(max_digits=6, decimal_places=3, blank=False, null=True, default=0)
    deltaD03 = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    D4 = models.DecimalField(max_digits=6, decimal_places=3, blank=False, null=True, default=0)
    deltaD4 = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)

    mAs = models.DecimalField(max_digits=7, decimal_places=3, blank=False, null=True, default=0)
    deltaMAS = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    kV = models.IntegerField(blank=True,null=True)
    diffKV = models.IntegerField(blank=True,null=True)

    DAP = models.DecimalField(max_digits=7,decimal_places=3,blank=True,null=True,default=0)
    deltaDAP = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)

    EI = models.DecimalField(max_digits=7, decimal_places=3, blank=False, null=True, default=0)
    deltaEI = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)
    EIt = models.DecimalField(max_digits=7, decimal_places=3, blank=False, null=True, default=0)
    DI = models.DecimalField(max_digits=7, decimal_places=3, blank=False, null=True, default=0)
    deltaDI = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True, default=0)

    baseline = models.BooleanField(blank=True,null=False, default=False)

    esitoSIGNAL = models.BooleanField(blank=True,null=True,default=True)
    esitoCONTRAST = models.BooleanField(blank=True, null=True, default=True)
    esitoSNR = models.BooleanField(blank=True, null=True, default=True)
    esitoSDNR = models.BooleanField(blank=True, null=True, default=True)
    esitoMTF50 = models.BooleanField(blank=True, null=True, default=True)
    esitoD03 = models.BooleanField(blank=True, null=True, default=True)
    esitoD4 = models.BooleanField(blank=True, null=True, default=True)

    comments = models.TextField(blank=True,null=True,)
    signal_image = models.BinaryField(null=True)



