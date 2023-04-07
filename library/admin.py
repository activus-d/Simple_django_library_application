from django.contrib import admin
from .models import Book, Author, Collection

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    prepopulated_fields = {"slug": ("name",)}

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author",)
    prepopulated_fields = {"slug": ("title",)}

class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Collection, CollectionAdmin)