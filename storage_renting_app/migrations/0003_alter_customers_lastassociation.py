# Generated by Django 3.2 on 2021-05-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_renting_app', '0002_rename_telefon_customers_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='lastAssociation',
            field=models.DateField(default=None, null=True),
        ),
    ]
