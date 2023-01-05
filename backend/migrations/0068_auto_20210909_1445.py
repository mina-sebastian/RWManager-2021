# Generated by Django 3.2 on 2021-09-09 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0067_auto_20210909_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='statie',
            name='au_fost',
            field=models.ManyToManyField(blank=True, related_name='au_fost', to='backend.GrupTH'),
        ),
        migrations.AddField(
            model_name='statie',
            name='echipe',
            field=models.ManyToManyField(blank=True, related_name='echipe', to='backend.GrupTH'),
        ),
        migrations.DeleteModel(
            name='Echipa',
        ),
    ]
