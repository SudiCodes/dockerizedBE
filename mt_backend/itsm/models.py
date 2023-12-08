from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Incident(models.Model):
    id = models.UUIDField(primary_key=True)
    incident_id = models.BigIntegerField(validators=[MinValueValidator(99999)])
    severity = models.IntegerField()
    impact = models.IntegerField()
    requester = models.EmailField()
    state = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField()
    last_updated_at = models.DateField()
    ci = models.CharField(max_length=10)
    subject = models.CharField(max_length=1023, default="No Subject")
    description = models.TextField(default="No Description")
    category = models.CharField(null=True, blank=True, default="Service")
    # assigned_to , resolved_at, closed_at,type,
