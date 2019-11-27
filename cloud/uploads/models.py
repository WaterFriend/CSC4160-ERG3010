from django.db import models
import uuid

# Create your models here.

class Patient(models.Model):
    pID         = models.AutoField(primary_key = True)
    pFName      = models.CharField(max_length = 20)
    pLName      = models.CharField(max_length = 20)
    pGender     = models.CharField(max_length = 10)
    pRace       = models.CharField(max_length = 20)
    pEthnicity  = models.CharField(max_length = 20)
    pAge        = models.IntegerField()

    def __str__(self):
        return self.pID

