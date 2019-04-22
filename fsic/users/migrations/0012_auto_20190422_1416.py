# Generated by Django 2.1.5 on 2019-04-22 14:16

import django.core.validators
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_merge_20190420_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='achievements',
            field=models.TextField(blank=True, default='Dedicated senior tennis player', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cien_no',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='home_club',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='images/', validators=[users.models.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role_model',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_email',
            field=models.EmailField(blank=True, max_length=254, validators=[django.core.validators.EmailValidator]),
        ),
    ]