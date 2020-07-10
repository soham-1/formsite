from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.

class details(models.Model):
    inctypes = (
        ('envIncident', 'envIncident'),
        ('injury_illness', 'injury_illness'),
        ('property', 'property'),
        ('vehicle', 'vehicle')
    )

    location = models.CharField(max_length=200, null=True, blank=True)
    incidentDesc = models.TextField(max_length=500, null=True, blank=True)
    incidentTime = models.TimeField(null=True, blank=True)
    incidentdate = models.DateField()
    inciloc = models.CharField(max_length=200)
    severity = models.CharField(max_length=50)
    cause = models.CharField(max_length=200)
    actionTaken = models.CharField(max_length=200)
    types = MultiSelectField(choices=inctypes, null=True, blank=True)
    reporter = models.CharField(max_length=100)
