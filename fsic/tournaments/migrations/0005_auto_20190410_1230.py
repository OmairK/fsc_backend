# Generated by Django 2.1.5 on 2019-04-10 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0004_auto_20190410_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournamentfsc',
            old_name='location_url',
            new_name='event_location_url',
        ),
    ]
