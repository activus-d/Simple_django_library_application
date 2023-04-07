"""
Tutorial on Django redirect: https://www.tutorialspoint.com/django/django_page_redirection.htm
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from library.models import Book, Collection, Author
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .forms import PostForm
from django.utils import timezone

# Create your views here.
@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, slug):
    single_book = get_object_or_404(Book, slug=slug)
    print(single_book)
    return render(request, 'library/book_detail.html', {'book': single_book})

def books_by_author(request, author_slug):
    author = get_object_or_404(Author, slug=author_slug)
    books = author.books.all()
    print(request)
    return render(request, 'library/books_by_author.html', {'books': books})

def collection_list(request):
    collections = Collection.objects.all()
    print(collections)
    return render(request, 'library/collection_list.html', {'collections': collections})

def collection_detail(request, slug):
    print(slug)
    books = Book.objects.filter(collection__slug=slug)
    return render(request, 'library/collection_detail.html', {'books': books})

def SearchResultsView(request):
    key = request.GET.get('search_key')
    search = Book.objects.get(Q(isbn__icontains=key) | Q(title__icontains=key) | Q(summary__icontains=key))
    return render(request, 'library/search_results.html', {'result': search})

def error_404(request, exception):
    return redirect(book_list)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
    else:
        form = PostForm()
    return render(request, 'library/post_edit.html', {'form': form})