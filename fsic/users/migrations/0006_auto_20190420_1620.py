# Generated by Django 2.1.5 on 2019-04-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190414_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(max_length=1000, null=True, upload_to=''),
        ),
    ]
