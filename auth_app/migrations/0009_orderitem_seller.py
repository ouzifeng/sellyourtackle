# Generated by Django 4.2.5 on 2023-10-11 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auth_app", "0008_orderitem_shipping_cost"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderitem",
            name="seller",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sold_items",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
