from django.contrib import admin
from core.models import CacheBarcode,BarcodeScanHit
# Register your models here.
class CacheBarcodeAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'last_updated', 'data')
admin.site.register(CacheBarcode, CacheBarcodeAdmin)


class BarcodeScanHitAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'timestemp',)
admin.site.register(BarcodeScanHit, BarcodeScanHitAdmin)