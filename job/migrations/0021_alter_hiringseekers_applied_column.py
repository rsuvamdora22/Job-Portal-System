# Generated by Django 5.1.4 on 2025-01-15 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0020_alter_hiringseekers_applied_column'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiringseekers',
            name='applied_column',
            field=models.CharField(default='you need to apply', max_length=50),
        ),
    ]
