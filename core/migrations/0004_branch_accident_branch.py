# Generated by Django 5.1.6 on 2025-02-07 16:14

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_accident_branch_delete_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='accident',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accidents', to='core.branch'),
        ),
    ]
