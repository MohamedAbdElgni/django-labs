# Generated by Django 5.0.2 on 2024-02-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="img",
            field=models.FileField(blank=True, null=True, upload_to="media/categories"),
        ),
        migrations.AlterField(
            model_name="product",
            name="img",
            field=models.FileField(blank=True, null=True, upload_to="media/products"),
        ),
    ]