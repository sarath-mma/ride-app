# Generated by Django 4.2.9 on 2024-02-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0006_tokendriver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='seat_capacity',
            field=models.CharField(choices=[('0', '4'), ('1', '7')], max_length=255, verbose_name='Vehicle Seat Capacity'),
        ),
    ]
