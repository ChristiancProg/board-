# Generated by Django 5.1.4 on 2025-01-09 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_topic_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='fecha',
        ),
    ]
