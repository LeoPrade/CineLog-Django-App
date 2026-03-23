from django.shortcuts import render, redirect
from .models import Movie, Review
from .utils import get_movie_from_omdb, search_movies_from_omdb, get_movie_from_id
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def movie_list(request):
    if request.user.is_authenticated:
        movies = Movie.objects.filter(review__user=request.user)
        search_word = request.GET.get('title', '')
        if search_word:
            movies = movies.filter(title__icontains=search_word)
        sort = request.GET.get('sort', '')
        if sort == 'imdb_rating':
            movies = movies.order_by('-imdb_rating')
        elif sort == 'personal_rating':
            movies = movies.order_by('-review__personal_rating')
        elif sort == 'newest':
            movies = movies.order_by('-review__created_at')
        elif sort == 'title':
            movies = movies.order_by('title')
        reviews = Review.objects.filter(user=request.user)
        paginator = Paginator(movies, 9)
        page_number = request.GET.get('page')
        movies = paginator.get_page(page_number)
    else:
        movies = []
        reviews = []
    return render(request, 'movies/index.html', {'movies': movies, 'reviews': reviews})

@login_required
def movie_add(request):
    if request.method == 'GET': 
        return render(request, 'movies/add.html')
    
    action = request.POST.get('action')
    if action == 'search':
        title = request.POST.get('title')
        data = search_movies_from_omdb(title)
        if data is None:
            return render(request, 'movies/add.html')
        movies = data['Search']
        return render(request, 'movies/add.html', {'movies': movies})
    
    elif action == 'add':
        movie_title = request.POST.get('title')
        data = get_movie_from_omdb(movie_title)
        if data is None:
            messages.error(request, 'Film nicht gefunden!')
            return redirect('movie_add')
        try:
            imdb_votes_nocomma = data["imdbVotes"].replace(",", "")
            imdb_votes_to_int = int(imdb_votes_nocomma)
            imdb_rating_to_float = float(data["imdbRating"])
        except ValueError:
            imdb_votes_to_int = 0
            imdb_rating_to_float = 0
        
        movie, created = Movie.objects.get_or_create(
            imdb_id=data['imdbID'],
            defaults={
                'title': data['Title'],
                'genre': data['Genre'],
                'release_year': data['Year'],
                'director': data['Director'],
                'awards': data['Awards'],
                'imdb_votes': imdb_votes_to_int,
                'imdb_id': data['imdbID'],
                'imdb_rating': imdb_rating_to_float,
                'poster_url': data['Poster'] if data['Poster'] != 'N/A' else None,
            }
        )
        
        review, created = Review.objects.get_or_create(
            movie=movie,
            user=request.user
        )
        
        if not created:
            messages.error(request, 'Dieser Film ist bereits in deiner Liste!')
            return redirect('movie_list')
        
        return redirect('movie_list')

def movie_search(request):
    if request.method == 'GET': 
        return render(request, 'movies/search.html')
    if request.method == 'POST':
        title = request.POST.get('title')
        if not title:
            return render(request, 'movies/search.html')
        data = search_movies_from_omdb(title)
        if data is None:
            return render(request, 'movies/search.html')
        else: 
            movies = data['Search']
        return render(request, 'movies/search.html', {'movies': movies})

@login_required
def my_list_search(request):
    title = request.GET.get('title', '')
    movies = Movie.objects.filter(review__user=request.user)
    if title:
        movies = movies.filter(title__icontains=title)
    return render(request, 'movies/my_list_search.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    review = Review.objects.filter(movie=movie, user=request.user).first()
    if request.method == 'POST':
        rating_input = request.POST.get('personal_rating')
        review.comment = request.POST.get('comment')
        if not rating_input:
            review.personal_rating = None
        else: 
            review.personal_rating = float(rating_input)
        review.save()
        
    return render(request, 'movies/detail.html', {'movie': movie, 'review': review})

@login_required
def movie_delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect('movie_list')

def movie_detail_omdb(request, imdb_id):
    data = get_movie_from_id(imdb_id)
    return render(request, 'movies/temp_detail.html', {'movie': data})