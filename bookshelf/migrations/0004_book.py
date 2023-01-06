# Generated by Django 4.1.5 on 2023-01-05 12:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0003_speaker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='book_title')),
                ('publish_year', models.DateField(null=True, verbose_name='publish_year')),
                ('date_published', models.DateTimeField(blank=None, default=datetime.datetime(2023, 1, 5, 15, 31, 45, 357461), null=None)),
                ('pages', models.IntegerField(verbose_name='book_page')),
                ('price', models.IntegerField(verbose_name='book_price')),
                ('book_author', models.ManyToManyField(to='bookshelf.author')),
                ('book_language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.language')),
            ],
        ),
    ]