# Generated by Django 4.1.6 on 2024-01-12 13:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_aff_mkt_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aff_mkt',
            name='body',
        ),
        migrations.AddField(
            model_name='sales',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
