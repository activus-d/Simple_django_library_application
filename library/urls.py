from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<title>/', views.book_detail, name='book_detail'),
    path("search/", views.SearchResultsView, name="search_results"),
]