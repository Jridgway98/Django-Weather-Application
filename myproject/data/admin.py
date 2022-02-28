from django.contrib import admin

from .models import City, Vehicle, Powerplant

admin.site.register(City)
admin.site.register(Vehicle)
admin.site.register(Powerplant)