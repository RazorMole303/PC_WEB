from django.db import models
from django.urls import reverse


class Product(models.Model):
    """One thing the shop sells.

    The category is a plain text choice rather than a second table. That keeps
    the number of things students have to think about right down.
    """

    CATEGORY_CHOICES = [
        ("cpu", "CPU"),
        ("gpu", "Graphics Card"),
        ("ram", "Memory"),
        ("storage", "Storage"),
        ("cooling", "Cooling"),
        ("case", "Case"),
        ("psu", "Power Supply"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=120)
    slug = models.SlugField(
        max_length=140,
        unique=True,
        help_text="A URL-friendly version of the name, e.g. 'ryzen-5-5600'.",
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default="other"
    )
    image = models.CharField(
        max_length=200,
        blank=True,
        help_text="Just the file name of an image in static/img, e.g. 'cpu-ryzen.svg'.",
    )
    stock = models.PositiveIntegerField(default=10)
    featured = models.BooleanField(
        default=False, help_text="Tick to show this on the home page."
    )

    class Meta:
        ordering = ["category", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", kwargs={"slug": self.slug})