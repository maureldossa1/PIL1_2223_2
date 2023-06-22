# Generated by Django 4.2.2 on 2023-06-18 14:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conexion', '0005_alter_programme_hrd_alter_programme_hrf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='hrd',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(7), django.core.validators.MaxValueValidator(19)], verbose_name='heure de debut'),
        ),
        migrations.AlterField(
            model_name='programme',
            name='hrf',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(7), django.core.validators.MaxValueValidator(19)], verbose_name='heurde fin'),
        ),
    ]