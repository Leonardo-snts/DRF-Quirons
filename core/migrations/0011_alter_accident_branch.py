# Generated by Django 5.1.6 on 2025-02-07 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_branch_accident_branch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accident',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.branch'),
        ),
    ]
