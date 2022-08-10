# Generated by Django 4.0.6 on 2022-07-18 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clothes", "0007_alter_cloth_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cloth",
            name="retail_price",
            field=models.PositiveIntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="cloth",
            name="sell_price",
            field=models.PositiveIntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
    ]
