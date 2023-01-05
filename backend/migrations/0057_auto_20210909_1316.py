# Generated by Django 3.2 on 2021-09-09 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0056_remove_grup_g_sid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Echipa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(default='', max_length=500)),
                ('telefon', models.CharField(max_length=10, unique=True)),
                ('persoane', models.SmallIntegerField()),
                ('dificultate', models.SmallIntegerField()),
                ('greenGym', models.BooleanField(default=True)),
                ('platite', models.SmallIntegerField(default=0)),
                ('baterie', models.SmallIntegerField(default=0)),
                ('incercari', models.TextField(blank=True, default='')),
                ('indicii', models.ManyToManyField(blank=True, to='backend.IndiciuMeta')),
                ('locatii', models.ManyToManyField(blank=True, to='backend.Locatie')),
                ('taskuri', models.ManyToManyField(blank=True, to='backend.TaskMeta')),
            ],
        ),
        migrations.AlterField(
            model_name='treasurehuntsettings',
            name='greu_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='greu_1', to='backend.echipa'),
        ),
        migrations.AlterField(
            model_name='treasurehuntsettings',
            name='greu_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='greu_2', to='backend.echipa'),
        ),
        migrations.AlterField(
            model_name='treasurehuntsettings',
            name='greu_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='greu_3', to='backend.echipa'),
        ),
        migrations.AlterField(
            model_name='treasurehuntsettings',
            name='greu_mentiune_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='greu_mentiune_1', to='backend.echipa'),
        ),
        migrations.AlterField(
            model_name='treasurehuntsettings',
            name='greu_mentiune_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='greu_mentiune_2', to='backend.echipa'),
        ),
        migrations.AlterField(
            model_name='treasurehuntsettings',
            name='mediu_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mediu_1', to='backend.echipa'),
        ),
        migrations.AlterField(
            model_name='treasurehuntsettings',
            name='mediu_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mediu_2', to='backend.echipa'),
        ),
        migrations.AlterField(
            model_name='treasurehuntsettings',
            name='mediu_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mediu_3', to='backend.echipa'),
        ),
        migrations.AlterField(
            model_name='treasurehuntsettings',
            name='mediu_mentiune_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mediu_mentiune_1', to='backend.echipa'),
        ),
        migrations.AlterField(
            model_name='treasurehuntsettings',
            name='mediu_mentiune_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mediu_mentiune_2', to='backend.echipa'),
        ),
        migrations.AlterField(
            model_name='treasurehuntsettings',
            name='tombola',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tombola', to='backend.echipa'),
        ),
        migrations.DeleteModel(
            name='Grup',
        ),
    ]
