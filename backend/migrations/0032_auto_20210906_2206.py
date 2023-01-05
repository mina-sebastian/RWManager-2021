# Generated by Django 3.2 on 2021-09-06 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0031_treasurehunt'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreasureHuntSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ora_incepere', models.DateTimeField()),
                ('ora_terminare', models.DateTimeField()),
                ('greu_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='greu_1', to='backend.echipa')),
                ('greu_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='greu_2', to='backend.echipa')),
                ('greu_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='greu_3', to='backend.echipa')),
                ('greu_mentiune_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='greu_mentiune_1', to='backend.echipa')),
                ('greu_mentiune_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='greu_mentiune_2', to='backend.echipa')),
                ('mediu_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mediu_1', to='backend.echipa')),
                ('mediu_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mediu_2', to='backend.echipa')),
                ('mediu_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mediu_3', to='backend.echipa')),
                ('mediu_mentiune_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mediu_mentiune_1', to='backend.echipa')),
                ('mediu_mentiune_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mediu_mentiune_2', to='backend.echipa')),
                ('tombola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tombola', to='backend.echipa')),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='poza',
            field=models.ImageField(blank=True, upload_to='incarcari/taskuri/%Y%m%d%H%M%S%s'),
        ),
        migrations.DeleteModel(
            name='TreasureHunt',
        ),
    ]
