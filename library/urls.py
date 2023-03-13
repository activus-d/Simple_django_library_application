from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<title>/', views.book_detail, name='book_detail'),
    path('<author>/', views.books_by_author, name='books_by_author'),
    path("search/", views.SearchResultsView, name="search_results"),
]