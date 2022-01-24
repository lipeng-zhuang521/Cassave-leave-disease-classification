from django.db import models

# Create your models here.
class ReportBikes(models.Model):
    # userId = models.CharField(max_length=100, null=True)
    bikeId = models.IntegerField(null=True)
    message = models.CharField(max_length=1000, null=True)