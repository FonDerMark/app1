from django.db import models


# Create your models here.
class Films(models.Model):
    name_ru = models.CharField(max_length=50, verbose_name='Название')
    name_en = models.CharField(max_length=50, verbose_name='Title')
    release_year = models.IntegerField(verbose_name='Year')
    film = models.FileField(verbose_name='Film', upload_to='films')
    description = models.TextField()

    class Meta:
        ordering = ['name_ru']
        verbose_name_plural = 'Films'