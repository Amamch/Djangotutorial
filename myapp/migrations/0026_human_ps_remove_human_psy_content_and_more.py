# Generated by Django 4.1.6 on 2024-01-10 13:24

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_remove_aff_mkt_pg_aff_mkt_2_pg_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='human_ps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', tinymce.models.HTMLField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('writer', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='human_psy',
            name='content',
        ),
        migrations.AddField(
            model_name='human_psy',
            name='created_at_1',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='human_psy',
            name='created_at_2',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='human_psy',
            name='title_2',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='human_psy',
            name='title_3',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
