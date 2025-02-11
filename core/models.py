from django.db import models

class Branch(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True)
    organizationId = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

class Accident(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True)
    accidentTypeEnum = models.CharField(max_length=50, null=True, blank=True)
    accidentPotential = models.CharField(max_length=50, null=True, blank=True)
    summary = models.CharField(max_length=255)  
    date = models.DateTimeField()
    timeWorked = models.DurationField(null=True, blank=True)
    description = models.TextField()
    street = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=False, blank=False)
    tag = models.CharField(max_length=255, null=True, blank=True)
    locomotion = models.CharField(max_length=255, null=True, blank=True)
    daysLost = models.IntegerField(null=True, blank=True)
    retired = models.BooleanField(null=True, blank=True, default=False)  # VERFICAR SE É BOOLEAN
    hasAbsence = models.BooleanField(null=True, blank=True, default=False)
    icd_code = models.CharField(max_length=50, null=True, blank=True)
    comunicationType = models.CharField(max_length=50, null=True, blank=True)
    person_age = models.IntegerField(null=True, blank=True)
    person_gender = models.CharField(max_length=50, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if self.locomotion:
            self.locomotion = self.locomotion.lower()  # Converte para minúsculas
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.summary
