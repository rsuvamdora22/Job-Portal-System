# Generated by Django 5.1 on 2024-10-05 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_recruiter_phno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=80)),
                ('pic', models.ImageField(upload_to='passphotos/')),
                ('email', models.EmailField(max_length=254)),
                ('psw', models.CharField(max_length=15)),
                ('phno', models.PositiveBigIntegerField()),
                ('gen', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('add', models.CharField(max_length=200)),
                ('hq', models.CharField(max_length=100)),
                ('un', models.CharField(max_length=200)),
                ('sd', models.DateField()),
                ('ed', models.DateField()),
                ('we', models.IntegerField()),
                ('pc', models.CharField(max_length=200)),
                ('pjt', models.CharField(max_length=50)),
                ('pjl', models.CharField(max_length=100)),
                ('atw', models.DateField()),
                ('ks', models.CharField(max_length=500)),
                ('lk', models.CharField(max_length=200)),
                ('intern', models.CharField(max_length=500)),
                ('proj', models.CharField(max_length=5000)),
                ('certi', models.CharField(max_length=1000)),
                ('ps', models.CharField(max_length=500)),
                ('resume', models.FileField(upload_to='pdfs/')),
            ],
        ),
    ]
