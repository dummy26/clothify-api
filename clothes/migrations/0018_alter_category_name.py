# Generated by Django 4.0.6 on 2022-08-21 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0017_remove_cartitem_cart_remove_cartitem_cloth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
