# Generated by Django 4.1.5 on 2023-02-15 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front_Pages', '0003_bg_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bg_images',
            name='bg_mode',
            field=models.CharField(choices=[('Portrait', 'Portrait'), ('Landscape', 'Landscape')], default='Landscape', max_length=20),
        ),
    ]
