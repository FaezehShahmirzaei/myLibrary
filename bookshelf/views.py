from django.shortcuts import render
from .models import Book


# Create your views here.

def book(request,bookname):
    return render(request, 'book.html')


# Create your views here.
def display_books(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})
