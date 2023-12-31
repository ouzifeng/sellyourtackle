# Generated by Django 4.2.5 on 2023-10-16 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0013_alter_order_payment_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("completed", "Completed"),
                    ("failed", "Failed"),
                    ("refunded", "Refunded"),
                    ("rf", "Refund Failed"),
                ],
                default="pending",
                max_length=10,
            ),
        ),
    ]
