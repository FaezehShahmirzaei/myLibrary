# Generated by Django 4.1.5 on 2023-01-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0009_remove_book_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobook',
            name='audiobooktime',
            field=models.IntegerField(default=0, verbose_name='Audiobook_time'),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='time',
            field=models.IntegerField(verbose_name='Podcast_time'),
        ),
    ]
