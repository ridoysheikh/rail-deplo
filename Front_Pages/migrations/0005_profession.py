# Generated by Django 4.1.5 on 2023-02-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front_Pages', '0004_alter_bg_images_bg_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=35)),
            ],
        ),
    ]