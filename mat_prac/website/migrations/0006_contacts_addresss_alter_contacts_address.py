# Generated by Django 4.1.7 on 2023-03-28 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='addresss',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
