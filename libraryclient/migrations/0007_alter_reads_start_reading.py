# Generated by Django 4.1.5 on 2023-01-06 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryclient', '0006_alter_reads_start_reading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reads',
            name='start_reading',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 6, 14, 52, 20, 402001)),
        ),
    ]
