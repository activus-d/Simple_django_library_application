from django.contrib import admin
from .models import Book, Author, Collection

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Collection)
