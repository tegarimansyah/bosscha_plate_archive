# Generated by Django 3.0.8 on 2020-07-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plate_archive', '0003_auto_20200711_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starobject',
            name='date',
            field=models.CharField(default='1970-01-01', max_length=10),
        ),
    ]
