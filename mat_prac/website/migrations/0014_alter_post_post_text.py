# Generated by Django 4.1.7 on 2023-03-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0013_webelement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_text",
            field=models.CharField(max_length=5000),
        ),
    ]