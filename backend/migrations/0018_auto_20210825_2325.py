# Generated by Django 3.2 on 2021-08-25 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_auto_20210825_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='indiciu',
            name='arataLocatie',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='indiciu',
            name='arataPoza',
            field=models.BooleanField(default=False),
        ),
    ]
