from django.db import models
from bookshelf.models import Book, Magazine, Audiobook, Podcast
from user.models import User
from datetime import datetime


# Create your models here.

class reads(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_read')
    magazin_id = models.ForeignKey(Magazine, on_delete=models.CASCADE, related_name='book_read')
    audiobook_id = models.ForeignKey(Audiobook, on_delete=models.CASCADE, related_name='book_read')
    podcast_id = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='book_read')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_read')
    status = models.CharField(max_length=5, choices=[('u', 'unread'), ('r', 'reading'), ('f', 'finished')])
    read_pages = models.IntegerField(null=False, default=0)
    start_reading = models.DateTimeField(default=datetime.now())

    def set_status(self, status_sit):
        self.status = status_sit
        self.save()

    def set_read_page(self, pagecount):
        self.read_pages = self.read_pages + pagecount
        self.save()
