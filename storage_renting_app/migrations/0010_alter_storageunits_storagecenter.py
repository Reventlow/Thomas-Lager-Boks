# Generated by Django 3.2 on 2021-05-09 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage_renting_app', '0009_auto_20210509_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storageunits',
            name='storageCenter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='storageunits_requests_created', to='storage_renting_app.storagecenters'),
        ),
    ]