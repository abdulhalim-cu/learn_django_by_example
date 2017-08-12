from django.contrib import admin

from .models import *


class ControlInstructionInline(admin.TabularInline):
    model = ControlInstruction


class DeviceStatesInline(admin.TabularInline):
    model = DeviceStates


class DeviceStatusInline(admin.TabularInline):
    model = DeviceStatus


class DeviceAdmin(admin.ModelAdmin):
    fields = ['device_name', 'device_model', 'location']
    inlines = [ControlInstructionInline, DeviceStatesInline, DeviceStatusInline]
    list_display = ('device_name', 'device_model', 'location')

admin.site.register(Device, DeviceAdmin)
