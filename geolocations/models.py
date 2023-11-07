# from django.db import models 
from django.contrib.gis.db import models 
from django.contrib.gis.geos import Point

# Create your models here.
class GeoLocation(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField(null=True,blank=True)  # Field to store latitude
    longitude = models.FloatField(null=True,blank=True)  # Field to store longitude
    location = models.PointField(geography=True, srid=4326)  # Geography field for storing latitude and longitude

 
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Create a Point object from the latitude and longitude fields
        self.location = Point(self.longitude, self.latitude, srid=4326)
        super(GeoLocation, self).save(*args, **kwargs)