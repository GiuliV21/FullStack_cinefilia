from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, CommentViewSet

from . import views

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/add_comment/', views.add_comment, name='add_comment'),
    path('api/', include(router.urls)),

]



