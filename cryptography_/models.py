from django.db import models


# Create your models here.
class CryptoFile(models.Model):
    encoded = models.BooleanField(blank=True)
    file = models.FileField(upload_to='cryptography/')
