from django.db import models

# Create your models here.

class BarcodeScanHit(models.Model):
    barcode = models.CharField(max_length=50)
    timestemp = models.DateTimeField(auto_now_add=True)