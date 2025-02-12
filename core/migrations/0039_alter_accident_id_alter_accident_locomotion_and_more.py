# Generated by Django 5.1.6 on 2025-02-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_alter_accident_id_alter_accident_locomotion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='accident',
            name='locomotion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='accident',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='accident',
            name='summary',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='accident',
            name='tag',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
