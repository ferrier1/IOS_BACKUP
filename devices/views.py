from django.shortcuts import render, get_object_or_404
from .models import Device
from django.http import HttpResponse, JsonResponse

def home(request):
    devices = Device.objects
    return render(request, 'devices/home.html', {'devices': devices})


def detail(request, device_id):
    if request.method == 'POST':
        device = get_object_or_404(Device, pk=device_id)
        name = device.hostname
        ip = device.ip
        vendor = device.vendor
        config = device.config
        print(config)
        return JsonResponse({'name': name, 'ip': ip, 'vendor': vendor, 'config': config})
    return render(request)
