from django.db import models

# Create your models here.
class Doctor(models.Model):
    dID         = models.AutoField(primary_key = True)
    dAccount    = models.CharField(max_length = 15)
    dPassword   = models.CharField(max_length = 255) 

    def __str__(self):
        return self.dID