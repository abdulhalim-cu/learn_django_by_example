from django.db import models
# import datetime
# from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=64, unique=True)
    device_name = models.CharField(max_length=100)
    device_model = models.CharField(max_length=10)
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.device_name


class ControlInstruction(models.Model):
    DIRECTION_CHOICES = (
        ('FW', 'Forward'),
        ('BW', 'Backward'),
    )
    # OneToOneField is is similar to a ForeignKey with unique=True, but the “reverse”
    # side of the relation will directly return a single object.
    device = models.OneToOneField(Device, on_delete=models.CASCADE, primary_key=True)
    on_off_flag = models.BooleanField(default=False)
    voltage_flag = models.FloatField(max_length=20, default=0)
    current_flag = models.FloatField(max_length=20, default=0)
    speed_flag = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    direction_flag = models.CharField(max_length=2, choices=DIRECTION_CHOICES)
    frequency_flag = models.IntegerField(default=0)


class Changes(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, primary_key=True)
    change = models.BooleanField(default=True)


class DeviceStatus(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, primary_key=True)
    created = models.DateTimeField('Creation date')
    last_connected = models.DateTimeField()


class DeviceStates(models.Model):
    device = models.OneToOneField(Device, on_delete=models.CASCADE, primary_key=True)
    on_or_off = models.BooleanField()
    voltage = models.CharField(max_length=20)
    current = models.CharField(max_length=20)
    speed = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    direction = models.CharField(max_length=2)
    frequency_flag = models.IntegerField(default=0)

