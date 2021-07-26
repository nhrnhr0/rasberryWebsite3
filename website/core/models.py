from django.db import models

# Create your models here.
class CacheBarcode(models.Model):
    barcode = models.CharField(max_length=120, unique=True)
    data = models.JSONField()
    last_updated = models.DateTimeField(auto_now=True)