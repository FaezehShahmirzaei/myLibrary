# Generated by Django 4.1.5 on 2023-01-06 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0010_alter_audiobook_audiobooktime_alter_podcast_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookreader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshelf.book')),
            ],
        ),
    ]