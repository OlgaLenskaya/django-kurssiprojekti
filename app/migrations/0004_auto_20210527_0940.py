# Generated by Django 3.2.3 on 2021-05-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AlterField(
            model_name='product',
            name='unitprice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
