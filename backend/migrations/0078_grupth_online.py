# Generated by Django 3.2 on 2021-09-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0077_indiciu_centru'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupth',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]
