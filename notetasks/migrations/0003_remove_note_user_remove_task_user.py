# Generated by Django 5.0.4 on 2024-04-24 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notetasks', '0002_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]