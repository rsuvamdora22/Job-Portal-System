# Generated by Django 5.1.1 on 2024-10-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0011_applicantdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantdetails',
            name='abtcomp',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='al',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='cl',
            field=models.ImageField(blank=True, null=True, upload_to='logos/'),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='er',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='exp',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='jd',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='jl',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='jr',
            field=models.CharField(max_length=4000, null=True),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='jtyp',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='kysk',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='ld',
            field=models.DateField(default='2025-01-01'),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='pos',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='applicantdetails',
            name='sal',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
