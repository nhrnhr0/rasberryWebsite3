from django.db import models

# Create your models here.
class CacheBarcode(models.Model):
    barcode = models.CharField(max_length=120, unique=True)
    data = models.JSONField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.barcode + ' - ' + self.data['catalog_images'][0]['title']

class BarcodeScanHit(models.Model):
    barcode = models.ForeignKey(to=CacheBarcode, on_delete=models.CASCADE)
    timestemp = models.DateTimeField(auto_now_add=True)

