from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<slug>/', views.book_detail, name='book_detail'),
    path('books/<author>/', views.books_by_author, name='books_by_author'),
    path('search/', views.SearchResultsView, name="search_results"),
    path('collections/', views.collection_list, name="collection_list"),
    path('collection/<name>', views.collection_detail, name="collection_detail"),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
