from django.shortcuts import render
import requests
import datetime
# Create your views here.
from django.utils import timezone

#EXPIRE_TIMER = datetime.timedelta(hours=24)
EXPIRE_TIMER = datetime.timedelta(minutes=2)

def home_view(request):
    return render(request,'index.html', {})

def video_view(request):
    return render(request, 'video.html', {})

from core.models import CacheBarcode
from online.models import BarcodeScanHit
def product_view(request, barcode):
    cached = CacheBarcode.objects.filter(barcode=barcode)
    barcode_data = None
    if(len(cached) == 0):
        resp = request_barcode_data(barcode)
        barcode_data = CacheBarcode.objects.create(barcode=barcode, data=resp)
        print('product: ', barcode_data.barcode, ' requested from the server and saved')
    else:
        barcode_data = cached.first()
        if barcode_data.last_updated + EXPIRE_TIMER < timezone.now():
            resp = request_barcode_data(barcode)
            
            barcode_data,created = CacheBarcode.objects.get_or_create(barcode=barcode)
            barcode_data.data = resp
            barcode_data.save()
            #CacheBarcode.objects.update(barcode=barcode, data=resp[0])
            #barcode_data = CacheBarcode.objects.get(barcode=barcode)
            #barcode_data.save()
            print('product: ', barcode_data.barcode, ' found in cached but updated')
        else:
            print('product: ', barcode_data.barcode, ' found and used from cached')
    print(BarcodeScanHit.objects.create(barcode=barcode_data.barcode))
        
    return render(request, 'product.html', {'data':barcode_data})


def request_barcode_data(barcode):
    response = requests.get(f'https://test.ms-global.co.il/api/barcode/{barcode}/')
    resp = response.json()
    if(resp == []):
        return None
    return resp[0]