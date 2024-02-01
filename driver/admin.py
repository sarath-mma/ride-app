from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin, StackedInline, GeoModelAdmin
from . models import Driver, Vehicle, Location
# Register your models here.

class VehicleAdmin(admin.StackedInline):

        model = Vehicle

class LoacationAdmin(StackedInline):
      
      model = Location

@admin.register(Driver)
class DriverAdmin(OSMGeoAdmin):
    list_display = ('name',)
    inlines = [VehicleAdmin, LoacationAdmin]


