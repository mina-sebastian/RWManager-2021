# Generated by Django 3.2 on 2021-09-09 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0055_delete_cookiemeta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grup',
            name='g_sid',
        ),
    ]