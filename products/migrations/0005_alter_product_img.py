# Generated by Django 5.0.2 on 2024-02-23 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_alter_category_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to="products/images"),
        ),
    ]