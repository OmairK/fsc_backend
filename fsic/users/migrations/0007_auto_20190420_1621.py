# Generated by Django 2.1.5 on 2019-04-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190420_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
