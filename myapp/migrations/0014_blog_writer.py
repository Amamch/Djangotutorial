# Generated by Django 4.1.6 on 2024-01-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_rename_sale_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
