# Generated by Django 4.1.6 on 2024-01-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_alter_sales_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
    ]