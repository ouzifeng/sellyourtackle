# Python standard library imports
from datetime import datetime
from decimal import Decimal

# Django core imports
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

# App-specific imports
from auth_app.models import Order


class Brand(models.Model):
    """
    Represents a brand in the database. Stores brand name.
    """
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "tackle_brand"

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Represents a category of products. Stores category name.
    """
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "tackle_category"

    def __str__(self):
        return self.name


class Condition(models.TextChoices):
    """
    Enum for product conditions,
    offering choices like Perfect, Excellent, Good, and Fair.
    """
    PERFECT = "Perfect",
    EXCELLENT = "Excellent",
    GOOD = "Good",
    FAIR = "Fair",

    def __str__(self):
        return f"{self.label} {self.additional_info}"


class FinancialStatus(models.TextChoices):
    """
    Enum for product visibility status, with choices like Draft and Live.
    """
    UNSOLD = 'unsold', 'Unsold'
    SOLD = 'sold', 'Sold'


class ProductVisibility(models.TextChoices):
    """
    Enum for product visibility status, with choices like Draft and Live.
    """
    DRAFT = 'draft', 'Draft'
    LIVE = 'live', 'Live'


class Product(models.Model):
    """
    Represents a product in the database. Stores details like brand, category,
    name, slug, condition, user, price, and shipping information.
    """
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=210, unique=True)
    variation1 = models.CharField(max_length=100, blank=True, null=True)
    variation2 = models.CharField(max_length=100, blank=True, null=True)
    condition = models.CharField(max_length=100, choices=Condition.choices)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00')
    )
    shipping = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal('0.00')
    )
    financial_status = models.CharField(
        max_length=10,
        choices=FinancialStatus.choices,
        default=FinancialStatus.UNSOLD
    )
    visibility = models.CharField(
        max_length=5,
        choices=ProductVisibility.choices,
        default=ProductVisibility.DRAFT
    )

    def is_in_stock(self):
        return self.financial_status == FinancialStatus.UNSOLD

    def __str__(self):
        return (
            f"Product id: {self.id}, name: {self.name}, "
            f"brand: {self.brand.name}, category: {self.category.name}, "
            f"condition: {self.condition}"
        )

    def save(self, *args, **kwargs):
        if not self.pk:
            slug_str = slugify(self.name)
            unique_slug = slug_str
            num = 1

            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{slug_str}-{num}"
                num += 1

            self.slug = unique_slug

        super(Product, self).save(*args, **kwargs)

    def total_with_shipping(self):
        return self.price + self.shipping


class ProductImage(models.Model):
    """
    Represents an image of a product.
    Links to the Product model and stores the image.
    """
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to=f"product-images/{datetime.now().strftime('%Y/%m/')}"
    )

    def __str__(self):
        return str(self.id)


class WebhookLog(models.Model):
    """
    Represents an image of a product.
    Links to the Product model and stores the image.
    """
    order = models.ForeignKey(
        Order, null=True, blank=True, on_delete=models.SET_NULL
    )
    payment_intent_id = models.CharField(max_length=255, null=True, blank=True)
    received_at = models.DateTimeField(auto_now_add=True)
    payload = models.TextField()
    header = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='received')
    event_type = models.CharField(max_length=255, null=True, blank=True)
