# Generated by Django 5.1 on 2024-10-16 16:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_appliedjobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedjobs',
            name='ad',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
