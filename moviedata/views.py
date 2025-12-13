from django.shortcuts import render, get_object_or_404
from .models import movie, shows


def movie_list(request):
    # Fetch all movies
    movies = movie.objects.all()
    return render(request, 'moviedata/movie_list.html', {'movies': movies})


def movie_detail(request, movie_id):
    # Fetch specific movie and its related shows
    selected_movie = get_object_or_404(movie, pk=movie_id)
    # Using the default reverse relationship name 'shows_set' since no related_name was defined in models
    movie_shows = selected_movie.shows_set.all().order_by('showtime')

    return render(request, 'moviedata/movie_detail.html', {
        'movie': selected_movie,
        'shows': movie_shows
    })