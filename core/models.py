from django.db import models
import uuid

class Accident(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    summary = models.CharField(max_length=255, unique=True)  # Evita duplicidade com um campo único
    date = models.DateTimeField()
    description = models.TextField()
    location_description = models.TextField(null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    social_security_affiliation = models.CharField(max_length=50)
    days_lost = models.IntegerField(null=True, blank=True)
    last_day_work = models.DateTimeField(null=True, blank=True)
    worked_hours = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.summary
