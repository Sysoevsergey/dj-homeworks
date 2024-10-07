from django.shortcuts import render, redirect
from .models import Book


def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    data = Book.objects.all()
    context = {}
    return render(request, template, context)
