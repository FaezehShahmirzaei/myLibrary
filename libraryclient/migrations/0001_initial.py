# Generated by Django 4.1.5 on 2023-01-06 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookshelf', '0012_delete_bookreader'),
        ('user', '0002_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookreader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('u', 'unread'), ('r', 'reading'), ('f', 'finished')], max_length=5)),
                ('read_pages', models.IntegerField(default=0)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_read', to='bookshelf.book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_read', to='user.user')),
            ],
        ),
    ]
