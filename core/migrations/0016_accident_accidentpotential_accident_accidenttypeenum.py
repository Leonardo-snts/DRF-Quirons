# Generated by Django 5.1.6 on 2025-02-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_accident_days_lost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='accidentPotential',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='accident',
            name='accidentTypeEnum',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
