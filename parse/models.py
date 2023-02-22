from django.db import models


# Create your models here.
class WeatherModel(models.Model):
    forecast_day = models.DateField()
    weather_dict = models.JSONField()
    coords = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    class Meta:
        unique_together = ('forecast_day', 'coords')

    def __str__(self):
        return self.forecast_day
