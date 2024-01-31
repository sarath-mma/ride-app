# Generated by Django 4.2.9 on 2024-01-30 18:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='license',
            field=models.ImageField(upload_to='license', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])], verbose_name='Driving License'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='picture',
            field=models.ImageField(upload_to='pictures', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])], verbose_name='Profile Picture'),
        ),
    ]