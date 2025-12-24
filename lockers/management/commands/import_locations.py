import csv
from django.core.management.base import BaseCommand
from lockers.models import Location

CATEGORY_MAP = {
    "supermarket": "SUPERMARKET",
    "fuel_station": "STATION",
    "bus_station": "GARE",
    "airport": "GARE",
}

class Command(BaseCommand):
    help = "Importer les emplacements depuis un fichier CSV"

    def handle(self, *args, **kwargs):
        path = "lockers/data/locations_senegal.csv"
        created, skipped = 0, 0

        with open(path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                name = row["name"].strip()
                lat = float(row["lat"])
                lng = float(row["lng"])

                # Éviter les doublons (nom + coordonnées)
                if Location.objects.filter(
                    name=name, latitude=lat, longitude=lng
                ).exists():
                    skipped += 1
                    continue

                Location.objects.create(
                    name=name,
                    location_type=CATEGORY_MAP.get(row["category"], "SUPERMARKET"),
                    region=row["region"],
                    department=row["department"],
                    commune=row["commune"],
                    latitude=lat,
                    longitude=lng,
                )
                created += 1

        self.stdout.write(self.style.SUCCESS(
            f"Import terminé ✅ {created} créés | {skipped} ignorés"
        ))
