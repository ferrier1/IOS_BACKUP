from django.db import models


class Device(models.Model):
    hostname = models.CharField(max_length=100)
    vendor = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    config = models.TextField()
