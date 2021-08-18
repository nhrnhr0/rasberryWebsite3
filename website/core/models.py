from django.db import models

# Create your models here.
class CacheBarcode(models.Model):
    barcode = models.CharField(max_length=120, unique=True)
    data = models.JSONField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        print('self.data', self.data)
        if self.data:
            try:
                title = self.data['catalog_images'][0]['title']
            except:
                title = 'error getting the title'
        else:
            title = str(self.data)
        return self.barcode + ' - ' + title



