# Generated by Django 5.1.6 on 2025-02-11 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_accident_dayslost'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='retired',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
