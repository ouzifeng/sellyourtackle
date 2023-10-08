# Generated by Django 4.2.5 on 2023-10-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0005_order_orderitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("paid", "Paid"),
                    ("shipped", "Shipped"),
                    ("delivered", "Delivered"),
                    ("refunded", "Refunded"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
    ]