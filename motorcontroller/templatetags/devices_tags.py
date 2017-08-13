from motorcontroller.models import Device
from django import template
# from django.contrib.auth.models import User

register = template.Library()


@register.inclusion_tag('motorcontroller/show_devices.html')
def show_devices(user):
    devices = Device.objects.filter(user=user)
    return {'devices': devices}

