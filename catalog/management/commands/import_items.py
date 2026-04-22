import csv
from pathlib import Path

from django.core.management.base import BaseCommand

from catalog.models import Category, Item

def floatParser(value):
    if value.strip() == "":
        return None
    try:
        return float(value)
    except ValueError:
        return None

def intParser(value):
    if value.strip() == "":
        return None
    try:
        return int(value)
    except ValueError:
        return None

class Command(BaseCommand):
    help = "Import movie data from the offline CSV datasets."

    def handle(self, *args, **options):
        data_dir = Path(__file__).resolve().parents[3] / "data"
        categories_path = data_dir / "categories.csv"
        items_path = data_dir / "movie.csv"

        categories_created = 0
        categories_updated = 0
        imported = 0
        updated = 0

        with categories_path.open(newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                _, created = Category.objects.update_or_create(
                    code="movies",
                    defaults={
                        "name": "Movies",
                        "description": "Movie dataset",
                    },
                )
                if created:
                    categories_created += 1
                else:
                    categories_updated += 1

        with items_path.open(newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                category = Category.objects.get(code="movies")
                _, created = Item.objects.update_or_create(
                    source_code=row["Movie_id"],
                    defaults={
                        "title": row["Title"],
                        "category": category,
                        "rating": floatParser(row["Rating"]),
                        "budget": intParser(row["Budget"]),
                        "currency": "USD",
                        #"currency": row["currency"],
                        "runtime": row["Runtime"],
                        "metacritic": intParser(row["MetaCritic"]),
                    },
                )
                if created:
                    imported += 1
                else:
                    updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                "Import complete: "
                f"{categories_created} categories created, "
                f"{categories_updated} categories updated, "
                f"{imported} items created, "
                f"{updated} items updated."
            )
        )
