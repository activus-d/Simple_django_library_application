from django import forms

from .models import Book

class PostForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'summary', 'isbn', 'slug', 'created_date', 'published_date')