# Generated by Django 4.1.6 on 2024-01-10 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_blog_created_at_1_blog_created_at_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
    ]
