# Generated by Django 4.1.6 on 2024-01-10 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_remove_sales_pg_sales_page_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales_pg',
            name='spt_1',
        ),
        migrations.RemoveField(
            model_name='sales_pg',
            name='spt_2',
        ),
        migrations.AddField(
            model_name='sales_pg',
            name='title_2',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='sales_pg',
            name='title_3',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
