from django.db import models

# Create your models here.
class ClimateData(models.Model):
    country = models.CharField(max_length=100)
    file = models.FileField(upload_to='climate_data')

    def __str__(self):
        return self.country

class CLimateGraphs(models.Model):
    country = models.CharField(max_length=100)
    file = models.ImageField(upload_to='climate_graphs')

    def __str__(self):
        return self.country