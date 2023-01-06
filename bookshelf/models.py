from django.db import models

from datetime import datetime, date, time


# Create your models here.


class Language(models.Model):
    language = models.CharField(max_length=35, blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.language}'


class Author(models.Model):
    author_name = models.CharField('author_name', max_length=40, null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.author_name}'


class Speaker(models.Model):
    speaker_name = models.CharField('peaker_name', max_length=40, null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.speaker_name}'


class Book(models.Model):
    title = models.CharField('book_title', max_length=100, null=False, unique=True)
    publish_year = models.DateField('publish_year', null=True)
    # date_published = models.DateTimeField(default=datetime.now(), blank=None, null=None)
    pages = models.IntegerField('book_page', null=False, blank=False)
    book_language = models.ForeignKey(Language, on_delete=models.CASCADE)
    book_author = models.ManyToManyField(Author)
    price = models.IntegerField('book_price', null=False, blank=False)

    def __str__(self):
        return f"{self.title}"


class Magazine(models.Model):
    title = models.CharField('magazine_title', max_length=100, null=False, unique=True)
    publish_year = models.DateField('publish_year', null=False, blank=False)
    pages = models.IntegerField('magazine_page', null=False, blank=False)
    magazine_language = models.ForeignKey(Language, on_delete=models.CASCADE)
    magazine_author = models.ManyToManyField(Author)
    price = models.IntegerField('magazine_price', null=False, blank=False)
    issue = models.CharField('issue', max_length=30, null=True)

    def __str__(self):
        return f'{self.title},{self.publish_year}'


class Podcast(models.Model):
    title = models.CharField('Podcast_title', max_length=100, null=False, unique=True)
    podcast_speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    publish_year = models.DateField('publish_year', null=False, blank=False)
    time = models.IntegerField('Podcast_time', null=False, blank=False)
    podcast_language = models.ForeignKey(Language, on_delete=models.CASCADE)
    price = models.IntegerField('Podcast_price', null=False, blank=False)

    def __str__(self):
        return f'{self.title},{self.time}minut,{self.podcast_speaker}'


class Audiobook(models.Model):
    title = models.CharField('Audiobook_title', max_length=100, null=False, unique=True)
    audiobook_speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    audiobook_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_year = models.DateField('publish_year', null=True, blank=False)
    pages = models.IntegerField(null=False, blank=False, default=0)
    audiobook_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='audiobook_language')
    audiobook_speaker_language = models.ForeignKey(Language, on_delete=models.CASCADE,
                                                   related_name='audiobook_speaker_language')
    audiobooktime = models.IntegerField('Audiobook_time', null=False, blank=False, default=0)
    audiobookprice = models.IntegerField('Audiobook_price', null=False, blank=False, default=0)


    def __str__(self):
        return f'{self.title},{self.audiobooktime} ,{self.audiobook_speaker_language}'

