# Generated by Django 4.1.7 on 2023-03-28 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_rename_contacts_contact_rename_socials_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='icon_link',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
