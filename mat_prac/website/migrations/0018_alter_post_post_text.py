# Generated by Django 4.1.7 on 2023-03-28 22:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0017_alter_post_img_alter_webelement_banner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="post_text",
            field=models.TextField(max_length=5000),
        ),
    ]