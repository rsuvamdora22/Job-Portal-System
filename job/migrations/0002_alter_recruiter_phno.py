# Generated by Django 5.1 on 2024-09-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='phno',
            field=models.PositiveBigIntegerField(),
        ),
    ]