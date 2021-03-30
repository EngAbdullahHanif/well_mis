# Generated by Django 3.1.7 on 2021-03-30 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Well',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('well_id', models.CharField(max_length=20)),
                ('well_type', models.CharField(max_length=30)),
                ('depth', models.IntegerField()),
                ('y', models.IntegerField()),
                ('x', models.IntegerField()),
                ('provence', models.CharField(max_length=15)),
                ('owener', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('EC_us_cm', models.IntegerField()),
                ('temprature', models.IntegerField()),
                ('PH', models.IntegerField()),
                ('salinity', models.IntegerField()),
                ('TDS_mg_lit', models.IntegerField()),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='well.well')),
            ],
        ),
    ]
