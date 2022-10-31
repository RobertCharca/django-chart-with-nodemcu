# Generated by Django 4.1.2 on 2022-10-30 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArduinoSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_name', models.CharField(max_length=200)),
                ('sensor_data_type', models.CharField(max_length=200)),
                ('sensor_value', models.CharField(max_length=10)),
            ],
        ),
    ]
