# Generated by Django 4.2.9 on 2024-01-31 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_driver_email_driver_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
