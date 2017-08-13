from django.contrib import admin

from .models import *


class ControlInstructionInline(admin.TabularInline):
    model = ControlInstruction


class DeviceStatesInline(admin.TabularInline):
    model = DeviceStates


class DeviceStatusInline(admin.TabularInline):
    model = DeviceStatus


class ChangesInline(admin.TabularInline):
    model = Changes

class DeviceAdmin(admin.ModelAdmin):
    fields = ['device_id', 'device_name', 'device_model', 'location']
    inlines = [ControlInstructionInline, DeviceStatesInline, DeviceStatusInline, ChangesInline]
    list_display = ('user', 'device_name', 'device_model', 'location')

admin.site.register(Device, DeviceAdmin)
