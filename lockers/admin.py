from django.contrib import admin
from .models import Location, Locker, UserProfile

admin.site.register(Location)
admin.site.register(Locker)
admin.site.register(UserProfile)
