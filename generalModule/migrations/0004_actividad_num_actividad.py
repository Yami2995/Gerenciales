# Generated by Django 4.0.4 on 2022-05-30 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalModule', '0003_remove_orden_fechazafra'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='num_actividad',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
