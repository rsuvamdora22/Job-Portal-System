# Generated by Django 5.1 on 2024-10-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_hiringseekers_cl'),
    ]

    operations = [
        migrations.AddField(
            model_name='hiringseekers',
            name='ld',
            field=models.DateField(default='2025-01-01'),
        ),
    ]