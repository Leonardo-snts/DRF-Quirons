# Generated by Django 5.1.6 on 2025-02-11 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_rename_icd_accident_icd_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='comunicationType',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='accident',
            name='timeWorked',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
