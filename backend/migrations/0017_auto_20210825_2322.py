# Generated by Django 3.2 on 2021-08-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_auto_20210825_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='locatie',
            name='directie',
            field=models.FloatField(default=-1),
        ),
        migrations.AlterField(
            model_name='locatie',
            name='viteza',
            field=models.FloatField(default=-1),
        ),
    ]
