# Generated by Django 4.2.9 on 2024-01-31 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_alter_driver_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='age',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='license',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='picture',
        ),
    ]
