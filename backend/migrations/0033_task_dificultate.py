# Generated by Django 3.2 on 2021-09-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0032_auto_20210906_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='dificultate',
            field=models.SmallIntegerField(default=0),
        ),
    ]