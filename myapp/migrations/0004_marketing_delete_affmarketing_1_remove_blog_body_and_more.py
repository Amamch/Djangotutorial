# Generated by Django 4.1.6 on 2023-12-29 03:37

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_affmarketing_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='marketing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', tinymce.models.HTMLField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='affmarketing_1',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='body',
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]