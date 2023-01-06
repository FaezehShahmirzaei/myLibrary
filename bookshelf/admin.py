from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Speaker)
admin.site.register(Book)
admin.site.register(Magazine)
admin.site.register(Podcast)
admin.site.register(Audiobook)