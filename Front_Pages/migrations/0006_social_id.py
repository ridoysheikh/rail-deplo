# Generated by Django 4.1.5 on 2023-02-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front_Pages', '0005_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='social_id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=35)),
                ('links', models.TextField(max_length=35)),
                ('logo_img', models.ImageField(upload_to='social_logo/front')),
            ],
        ),
    ]