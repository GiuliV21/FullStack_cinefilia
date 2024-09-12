from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, CommentViewSet, movie_list, add_comment
from .views import PopularMoviesView, RecommendedMoviesView, NewReleasesMoviesView




from . import views

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('movies/<int:profile_id>/', movie_list, name='movie_list'),
    path('movies/comment/<int:movie_id>/', add_comment, name='add_comment'),
    path('movie/<int:movie_id>/add_comment/', views.add_comment, name='add_comment'),
    path('api/movies/popular/', PopularMoviesView.as_view(), name='popular_movies'),
    path('api/movies/recommended/', RecommendedMoviesView.as_view(), name='recommended_movies'),
    path('api/movies/new-releases/', NewReleasesMoviesView.as_view(), name='new_releases_movies'),
    path('api/', include(router.urls)),

]



