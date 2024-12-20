# Generated by Django 5.1.1 on 2024-10-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_applicantdetails_progress_percentage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantdetails',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('under_review', 'Under_Review'), ('shortlisted', 'Shortlisted'), ('hired', 'Hired')], default='applied', max_length=20, null=True),
        ),
    ]
