from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lockers.models import UserProfile, Location, Locker

class Command(BaseCommand):
    help = 'Populate Pelicoli database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Locker.objects.all().delete()
        Location.objects.all().delete()
        
        # Create UserProfiles
        admin_user = User.objects.get(username='admin')
        UserProfile.objects.get_or_create(
            user=admin_user,
            defaults={'role': 'ADMIN'}
        )
        
        # Create Locations
        locations_data = [
            # Auchan (Supermarkets)
            {
                'name': 'Auchan Plateau',
                'location_type': 'SUPERMARKET',
                'region': 'Dakar',
                'department': 'Dakar',
                'commune': 'Plateau',
                'latitude': 14.6737,
                'longitude': -17.4414
            },
            {
                'name': 'Auchan Liberté 5',
                'location_type': 'SUPERMARKET',
                'region': 'Dakar',
                'department': 'Dakar',
                'commune': 'Liberté',
                'latitude': 14.6890,
                'longitude': -17.4565
            },
            {
                'name': 'Auchan HLM',
                'location_type': 'SUPERMARKET',
                'region': 'Dakar',
                'department': 'Dakar',
                'commune': 'HLM',
                'latitude': 14.7078,
                'longitude': -17.4523
            },
            
            # Stations-service
            {
                'name': 'Total Liberté 6',
                'location_type': 'STATION',
                'region': 'Dakar',
                'department': 'Dakar',
                'commune': 'Liberté',
                'latitude': 14.6920,
                'longitude': -17.4590
            },
            {
                'name': 'Shell AIBD Route',
                'location_type': 'STATION',
                'region': 'Dakar',
                'department': 'Dakar',
                'commune': 'Yoff',
                'latitude': 14.7450,
                'longitude': -17.4950
            },
            {
                'name': 'Total Pikine Icotaf',
                'location_type': 'STATION',
                'region': 'Dakar',
                'department': 'Pikine',
                'commune': 'Pikine',
                'latitude': 14.7500,
                'longitude': -17.4000
            },
            
            # Gares routières
            {
                'name': 'Gare Routière des Baux Maraîchers',
                'location_type': 'GARE',
                'region': 'Dakar',
                'department': 'Pikine',
                'commune': 'Pikine',
                'latitude': 14.7450,
                'longitude': -17.4050
            },
            {
                'name': 'Gare Pétersen',
                'location_type': 'GARE',
                'region': 'Dakar',
                'department': 'Dakar',
                'commune': 'Plateau',
                'latitude': 14.6720,
                'longitude': -17.4420
            },
            {
                'name': 'Gare Colobane',
                'location_type': 'GARE',
                'region': 'Dakar',
                'department': 'Dakar',
                'commune': 'Médina',
                'latitude': 14.6850,
                'longitude': -17.4550
            },
        ]
        
        for loc_data in locations_data:
            location = Location.objects.create(**loc_data)
            
            # Create 2 lockers per location
            Locker.objects.create(
                location=location,
                code=f"LOC-{location.commune[:3].upper()}-{location.id:03d}-A",
                is_active=True
            )
            Locker.objects.create(
                location=location,
                code=f"LOC-{location.commune[:3].upper()}-{location.id:03d}-B",
                is_active=True
            )
        
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created:\n'
            f'- {Location.objects.count()} locations\n'
            f'- {Locker.objects.count()} lockers'
        ))