# Generated by Django 4.1.5 on 2023-01-05 12:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0007_alter_book_date_published_audiobook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_published',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2023, 1, 5, 15, 51, 44, 800942), null=None),
        ),
    ]
