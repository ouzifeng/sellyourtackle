# Generated by Django 4.2.5 on 2023-10-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0011_customuser_is_stripe_verified"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="tracking_company",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="tracking_number",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
