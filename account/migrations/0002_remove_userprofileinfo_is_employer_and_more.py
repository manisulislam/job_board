# Generated by Django 4.2.7 on 2024-01-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='is_employer',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='is_jobseeker',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='user_types',
            field=models.CharField(blank=True, choices=[('EMPLOYER', 'EMPLOYER'), ('JOBSEEKER', 'JOBSEEKER')], max_length=20, null=True),
        ),
    ]