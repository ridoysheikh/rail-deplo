# Generated by Django 4.1.3 on 2023-03-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Front_Pages', '0016_alter_contact_info_adresses_alter_contact_info_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='logo_img',
            field=models.ImageField(upload_to='market/front'),
        ),
    ]