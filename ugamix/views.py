from django.shortcuts import render, get_object_or_404
from .models import Category, Movie
# Create your views here.
def index(request):
    all_categories = Category.objects.all()
    all_movies = Movie.objects.all()
    context = {
        'all_categories': all_categories,
        'all_movies': all_movies
    }
    return render(request, 'index.html', context)

def detail(request, movie_id):
    movies = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movies': movies
    }
    return render(request, 'moviesingle.html', context)

def AllMovies(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'category': category
    }
    return render(request, 'moviegridfw.html', context)