# Generated by Django 4.1.6 on 2024-01-12 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_alter_aff_mkt_pg_options_alter_human_psy_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sales_pg',
            options={'ordering': ['created_at']},
        ),
    ]