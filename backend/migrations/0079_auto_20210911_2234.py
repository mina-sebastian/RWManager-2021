# Generated by Django 3.2 on 2021-09-11 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0078_grupth_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupth',
            name='alerte',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='grupth',
            name='directie',
            field=models.SmallIntegerField(default=0),
        ),
    ]
