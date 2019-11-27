from django.db import models

# Create your models here.
class Doctor(models.Model):
    dID         = models.AutoField(primary_key = True)
    dName       = models.CharField(max_length = 30)
    dAccount    = models.CharField(max_length = 30)
    dPassword   = models.CharField(max_length = 30)