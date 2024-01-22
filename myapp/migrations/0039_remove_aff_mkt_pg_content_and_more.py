# Generated by Django 4.1.6 on 2024-01-12 17:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_amp1_amp2_amp3_hmp1_hmp2_hmp3_sp1_sp2_sp3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aff_mkt_pg',
            name='content',
        ),
        migrations.RemoveField(
            model_name='aff_mkt_pg',
            name='content_1',
        ),
        migrations.RemoveField(
            model_name='aff_mkt_pg',
            name='content_2',
        ),
        migrations.RemoveField(
            model_name='human_psy',
            name='content',
        ),
        migrations.RemoveField(
            model_name='human_psy',
            name='content_1',
        ),
        migrations.RemoveField(
            model_name='human_psy',
            name='content_2',
        ),
        migrations.RemoveField(
            model_name='sales_pg',
            name='content',
        ),
        migrations.RemoveField(
            model_name='sales_pg',
            name='content_1',
        ),
        migrations.AddField(
            model_name='amp1',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='amp1',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='amp1',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='amp1',
            name='writer',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='amp2',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='amp2',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='amp2',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='amp2',
            name='writer',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='amp3',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='amp3',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='amp3',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='amp3',
            name='writer',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='hmp1',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='hmp1',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='hmp1',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='hmp1',
            name='writer',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='hmp2',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='hmp2',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='hmp2',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='hmp2',
            name='writer',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='hmp3',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='hmp3',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='hmp3',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='hmp3',
            name='writer',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='sp1',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='sp1',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='sp1',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='sp1',
            name='writer',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='sp2',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='sp2',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='sp2',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='sp2',
            name='writer',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='sp3',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='sp3',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='image/'),
        ),
        migrations.AddField(
            model_name='sp3',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='sp3',
            name='writer',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='aff_mkt_pg',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='human_psy',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='sales_pg',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
