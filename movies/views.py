
from rest_framework import viewsets
from .serializers import MovieSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from .serializers import CommentSerializer
from .models import Movie  
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status





class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



# def movie_list(request, profile_id):
#     # Obtener todas las películas, puedes agregar filtros más adelante si es necesario
#     all_movies = Movie.objects.all()

#     # Dividir las películas en categorías
#     popular_movies = all_movies.filter(category="Popular")[:10]
#     recommended_movies = all_movies.filter(category="Recommended")[:10]
#     new_releases = all_movies.filter(category="New Release")[:10]

#     context = {
#         'profile_id': profile_id,
#         'popular_movies': popular_movies,
#         'recommended_movies': recommended_movies,
#         'new_releases': new_releases,
#     }

#     return render(request, 'movie/movie_list.html', context)


def movie_list(request, profile_id):
    # Obtener todas las películas, puedes agregar filtros más adelante si es necesario
    all_movies = Movie.objects.all()

    # Dividir las películas en categorías
    popular_movies = all_movies.filter(category="Popular")[:10]
    recommended_movies = all_movies.filter(category="Recommended")[:10]
    new_releases = all_movies.filter(category="New Release")[:10]

    context = {
        'profile_id': profile_id,
        'popular_movies': popular_movies,
        'recommended_movies': recommended_movies,
        'new_releases': new_releases,
    }

    return render(request, 'movies/movie_list.html', context)

# @login_required
# def add_comment(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.movie = movie
#             comment.user = request.user
#             comment.save()
#             return redirect('movie_list')
#     else:
#         form = CommentForm()
#     return render(request, 'movies/add_comment.html', {'form': form, 'movie': movie})

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
            return redirect('movie_detail', movie_id=movie.id)  # Redirige a la página de detalles de la película
    else:
        form = CommentForm()

    return render(request, 'movies/add_comment.html', {'form': form, 'movie': movie})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

@login_required
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    comments = Comment.objects.filter(movie=movie)
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'comments': comments})

class PopularMoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(is_popular=True)  # Asumiendo que tienes un campo is_popular
        serializer = MovieSerializer(movies, many=True)
        return Response({"movies": serializer.data}, status=status.HTTP_200_OK)

class RecommendedMoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(is_recommended=True)  # Asumiendo que tienes un campo is_recommended
        serializer = MovieSerializer(movies, many=True)
        return Response({"movies": serializer.data}, status=status.HTTP_200_OK)

class NewReleasesMoviesView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(release_date__gte=datetime.date.today())  # Asumiendo que tienes un campo release_date
        serializer = MovieSerializer(movies, many=True)
        return Response({"movies": serializer.data}, status=status.HTTP_200_OK)