from django.db import models
import uuid

# Create your models here.

class Patient(models.Model):
    pID         = models.AutoField(primary_key = True)
    pFName      = models.CharField(max_length = 30,  null=False)
    pLName      = models.CharField(max_length = 30,  null=False)
    pGender     = models.CharField(max_length = 10,  null=False)
    pRace       = models.CharField(max_length = 20,  null=False)
    pEthnicity  = models.CharField(max_length = 20,  null=True)
    pStatus     = models.CharField(max_length = 5,   null=False)
    pRemark     = models.CharField(max_length = 255, null=True)
    pAge        = models.IntegerField()
    dID         = models.ForeignKey('login.Doctor', on_delete = models.CASCADE)

    def __str__(self):
        return self.pID


# class Doctor(models.Model):
#     dID         = models.AutoField(primary_key = True)
#     dAccount    = models.CharField(max_length = 15)
#     dPassword   = models.CharField(max_length = 255) 

#     def __str__(self):
#         return self.dID
