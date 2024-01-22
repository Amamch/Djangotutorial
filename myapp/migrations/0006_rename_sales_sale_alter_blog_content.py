# Generated by Django 4.1.6 on 2024-01-05 22:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_affmkt_humpsy_sales'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sales',
            new_name='sale',
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]