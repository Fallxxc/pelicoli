
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("ADMIN", "Administrateur"),
        ("OPERATOR", "Opérateur"),
        ("VIEWER", "Consultation"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="VIEWER")

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Location(models.Model):
    LOCATION_TYPE_CHOICES = [
        ("SUPERMARKET", "Supermarché"),
        ("STATION", "Station-service"),
        ("GARE", "Gare routière"),
    ]

    name = models.CharField(max_length=255, null=True, blank=True)
    location_type = models.CharField(max_length=20, choices=LOCATION_TYPE_CHOICES)
    region = models.CharField(max_length=100,null=True, blank=True)
    department = models.CharField(max_length=100,null=True, blank=True)
    commune = models.CharField(max_length=100,null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name} - {self.commune}"


class Locker(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="lockers", blank=True, null=True  )
    code = models.CharField(max_length=50, unique=True , null=True, blank=True)
    is_active = models.BooleanField(default=True)
    installed_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Locker {self.code} @ {self.location.name}"

