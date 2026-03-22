from django.urls import path
from .views import movie_list, movie_detail, movie_search, movie_add, movie_delete, my_list_search, movie_detail_omdb

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('add/', movie_add, name='movie_add'),
    path('search/', movie_search, name='movie_search'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('movie/<int:movie_id>/delete/', movie_delete, name='movie_delete'),
    path('my_list/search/', my_list_search, name='my_list_search'),
    path('temp_detail/<str:imdb_id>/', movie_detail_omdb, name='temp_detail'),
]