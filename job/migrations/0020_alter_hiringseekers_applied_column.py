# Generated by Django 5.1.4 on 2025-01-15 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0019_hiringseekers_applied_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiringseekers',
            name='applied_column',
            field=models.BooleanField(default='Apply'),
        ),
    ]
