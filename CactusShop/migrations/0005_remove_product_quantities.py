# Generated by Django 4.0 on 2022-01-26 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CactusShop', '0004_rename_quantityy_product_quantities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Quantities',
        ),
    ]
