# Generated by Django 4.1.6 on 2024-01-12 13:53

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_alter_blog_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='aff_mkt',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
