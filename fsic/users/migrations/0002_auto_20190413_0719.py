# Generated by Django 2.1.5 on 2019-04-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='contact_no',
            field=models.BigIntegerField(null=True),
        ),
    ]
