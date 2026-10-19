from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from shop.models import Product

PRODUCTS = [
    {
        "slug": "amd-ryzen-5-5600",
        "name": "AMD Ryzen 5 5600",
        "category": "cpu",
        "price": "129.99",
        "stock": 12,
        "featured": True,
        "image": "cpu-ryzen.svg",
        "description": "Six cores, twelve threads. The best-value gaming CPU "
        "of its generation and still easy to cool.",
    },
    {
        "slug": "intel-core-i5-12400f",
        "name": "Intel Core i5-12400F",
        "category": "cpu",
        "price": "139.99",
        "stock": 8,
        "featured": False,
        "image": "cpu-intel.svg",
        "description": "Six performance cores with a boost clock of 4.4GHz. "
        "No integrated graphics, so you will need a graphics card.",
    },
    {
            "slug": "Corsair Case",
            "name": "Corsair Case",
            "category": "case",
            "price": "99.99",
            "stock": 50,
            "featured": False,
            "image": "case-tower.svg",
            "description": "An ATX sized case for your motherboard, spacious for whatever hardware you wish to fit "
            "Comes with 6 pre installed fans",
        },
    # ... nine more, in the same shape ...
]


class Command(BaseCommand):
    help = "Load sample products into the database."

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete every existing product first.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options["clear"]:
            deleted, _ = Product.objects.all().delete()
            self.stdout.write(
                self.style.WARNING(f"Deleted {deleted} existing products.")
            )

        created_count = 0
        updated_count = 0

        for data in PRODUCTS:
            data = dict(data, price=Decimal(data["price"]))
            slug = data.pop("slug")

            product, created = Product.objects.update_or_create(
                slug=slug, defaults=data
            )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Done. Created {created_count}, updated {updated_count}. "
                f"The shop now has {Product.objects.count()} products."
            )
        )