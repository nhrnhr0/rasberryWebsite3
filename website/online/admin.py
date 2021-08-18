from django.contrib import admin
from .models import BarcodeScanHit
# Register your models here.
class BarcodeScanHitAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'timestemp',)
admin.site.register(BarcodeScanHit, BarcodeScanHitAdmin)