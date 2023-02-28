"""
Tutorial on Django redirect: https://www.tutorialspoint.com/django/django_page_redirection.htm
"""
from django.shortcuts import render, redirect
from library.models import Book
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, title):
    single_book = get_object_or_404(Book, title=title)
    print(single_book)
    return render(request, 'library/book_detail.html', {'book': single_book})

class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'

def error_404(request, exception):
    return redirect(book_list)