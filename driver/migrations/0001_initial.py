# Generated by Django 4.2.9 on 2024-01-30 16:36

import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Full name')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('0', 'male'), ('1', 'female'), ('2', 'others')], max_length=255)),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '9999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Contact Number')),
                ('picture', models.ImageField(upload_to='pictures', verbose_name='Profile Picture')),
                ('license', models.ImageField(upload_to='license', verbose_name='Driving License')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('brand', models.CharField(max_length=255, verbose_name='Vehicle Brand')),
                ('model', models.CharField(max_length=255, verbose_name='Vehicle Model')),
                ('reg_year', models.CharField(choices=[('1990', 1990), ('1991', 1991), ('1992', 1992), ('1993', 1993), ('1994', 1994), ('1995', 1995), ('1996', 1996), ('1997', 1997), ('1998', 1998), ('1999', 1999), ('2000', 2000), ('2001', 2001), ('2002', 2002), ('2003', 2003), ('2004', 2004), ('2005', 2005), ('2006', 2006), ('2007', 2007), ('2008', 2008), ('2009', 2009), ('2010', 2010), ('2011', 2011), ('2012', 2012), ('2013', 2013), ('2014', 2014), ('2015', 2015), ('2016', 2016), ('2017', 2017), ('2018', 2018), ('2019', 2019), ('2020', 2020), ('2021', 2021), ('2022', 2022), ('2023', 2023), ('2024', 2024)], max_length=255, verbose_name='Vehicle Registerd Year')),
                ('type', models.CharField(choices=[('0', 'sedan'), ('1', 'hatchback'), ('1', 'suv')], max_length=255, verbose_name='Vehicle Type')),
                ('seat_capacity', models.CharField(choices=[('0', '4'), ('0', '7')], max_length=255, verbose_name='Vehicle Seat Capacity')),
                ('boot', models.CharField(choices=[('0', '330L'), ('1', '600L'), ('1', '1200L')], max_length=255, verbose_name='Vehicle Boot Capacity')),
                ('charge', models.IntegerField(verbose_name='Taxi charge/km')),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver_vehicle', to='driver.driver')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('driver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='driver_location', to='driver.driver')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]