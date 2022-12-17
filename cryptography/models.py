from django.db import models


# Create your models here.
class CryptoFile(models.Model):
    encoded = models.BooleanField()
    file = models.FileField(upload_to='cryptography/')



    def __str__(self):
        return self.file.name
