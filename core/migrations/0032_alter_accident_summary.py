# Generated by Django 5.1.6 on 2025-02-11 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_alter_accident_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='summary',
            field=models.CharField(max_length=255),
        ),
    ]
