"""
Tutorial on Django redirect: https://www.tutorialspoint.com/django/django_page_redirection.htm
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from library.models import Book, Collection
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, title):
    single_book = get_object_or_404(Book, title=title)
    print(single_book)
    return render(request, 'library/book_detail.html', {'book': single_book})

def books_by_author(request, author):
    books = Book.objects.filter(author__name=author).values()
    print(request)
    return render(request, 'library/books_by_author.html', {'books': books})

def collection_list(request):
    collections = Collection.objects.all()
    print(collections)
    return render(request, 'library/collection_list.html', {'collections': collections})

def collection_detail(request, name):
    print(name)
    books = Book.objects.filter(collection__name=name)
    print(books)
    return render(request, 'library/collection_detail.html', {'books': books})

def SearchResultsView(request):
    key = request.GET.get('search_key')
    search = Book.objects.get(Q(isbn__icontains=key) | Q(title__icontains=key) | Q(summary__icontains=key))
    return render(request, 'library/search_results.html', {'result': search})

def error_404(request, exception):
    return redirect(book_list)