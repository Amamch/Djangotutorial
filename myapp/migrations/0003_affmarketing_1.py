# Generated by Django 4.1.6 on 2023-12-20 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_blog_delete_marketing_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='affmarketing_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('body', models.CharField(max_length=3000000)),
                ('created_at', models.DateTimeField(default=datetime.datetime)),
            ],
        ),
    ]
