# Generated by Django 5.1.6 on 2025-02-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_accident_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='accident',
            name='locomotion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
