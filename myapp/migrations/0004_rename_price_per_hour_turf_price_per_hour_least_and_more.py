# Generated by Django 5.0.6 on 2024-05-13 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_turf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turf',
            old_name='price_per_hour',
            new_name='price_per_hour_least',
        ),
        migrations.AddField(
            model_name='turf',
            name='price_per_hour_max',
            field=models.IntegerField(default=0),
        ),
    ]
