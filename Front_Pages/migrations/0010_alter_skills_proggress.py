# Generated by Django 4.1.5 on 2023-02-17 10:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front_Pages', '0009_rename_description_skills_proggress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='proggress',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
