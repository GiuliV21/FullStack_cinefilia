
from rest_framework import viewsets
from .serializers import MovieSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from .serializers import CommentSerializer



class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

@login_required
def add_comment(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect('movie_list')
    else:
        form = CommentForm()
    return render(request, 'movies/add_comment.html', {'form': form, 'movie': movie})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer