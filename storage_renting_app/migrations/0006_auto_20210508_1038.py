# Generated by Django 3.2 on 2021-05-08 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage_renting_app', '0005_auto_20210508_0737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storageunits',
            old_name='rentedToId',
            new_name='rentedTo',
        ),
        migrations.RenameField(
            model_name='storageunits',
            old_name='storagecenterId',
            new_name='storageCenter',
        ),
    ]
