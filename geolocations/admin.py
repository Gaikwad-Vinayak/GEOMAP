from django.contrib import admin
from geolocations.models import GeoLocation
# Register your models here.


@admin.register(GeoLocation)
class GeoLocationAdmin(admin.ModelAdmin):
    list_display = ['id','name']