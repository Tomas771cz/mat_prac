# Generated by Django 4.1.7 on 2023-03-28 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_contacts_addresss_alter_contacts_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='addresss',
            new_name='person',
        ),
    ]
