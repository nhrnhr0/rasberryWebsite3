from django.contrib import admin
from core.models import CacheBarcode
# Register your models here.
class CacheBarcodeAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'last_updated', 'data')
admin.site.register(CacheBarcode, CacheBarcodeAdmin)


