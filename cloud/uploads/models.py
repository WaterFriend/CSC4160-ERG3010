from django.db import models
import uuid

# Create your models here.

class Patient(models.Model):
    pID         = models.AutoField(primary_key = True)
    pFName      = models.CharField(max_length = 30)
    pLName      = models.CharField(max_length = 30)
    pGender     = models.CharField(max_length = 10)
    pRace       = models.CharField(max_length = 20)
    pEthnicity  = models.CharField(max_length = 20)
    pStatus     = models.CharField(max_length = 5)
    pRemark     = models.CharField(max_length = 255)
    pAge        = models.IntegerField()
    dID         = models.ForeignKey('Doctor', on_delete = models.CASCADE)

    def __str__(self):
        return self.pID

class Doctor
