# Generated by Django 3.2 on 2021-08-26 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_indiciu_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Punct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=400)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='participanti',
        ),
        migrations.AddField(
            model_name='echipa',
            name='incercari',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='echipa',
            name='nume',
            field=models.CharField(max_length=500),
        ),
        migrations.DeleteModel(
            name='Statie',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='punct',
            name='echipa',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.echipa'),
        ),
        migrations.AddField(
            model_name='punct',
            name='locatie',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='backend.locatie'),
        ),
    ]
