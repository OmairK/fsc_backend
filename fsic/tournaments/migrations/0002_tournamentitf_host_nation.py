# Generated by Django 2.1.5 on 2019-03-14 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentitf',
            name='host_nation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
