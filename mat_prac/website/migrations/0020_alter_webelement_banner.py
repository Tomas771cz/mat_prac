# Generated by Django 4.1.7 on 2023-03-29 19:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0019_soupiska"),
    ]

    operations = [
        migrations.AlterField(
            model_name="webelement",
            name="banner",
            field=models.ImageField(upload_to="static/"),
        ),
    ]
