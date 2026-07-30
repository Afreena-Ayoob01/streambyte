from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'movie/<int:movie_id>/',
        views.movie_detail,
        name='movie_detail'
    ),

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),

    path(
        'add-movie/',
        views.add_movie,
        name='add_movie'
    ),

    path(
        'movie/<int:movie_id>/edit/',
        views.edit_movie,
        name='edit_movie'
    ),

    path(
        'movie/<int:movie_id>/delete/',
        views.delete_movie,
        name='delete_movie'
    ),

    path(
    'movie/<int:movie_id>/favorite/',
    views.add_favorite,
    name='add_favorite'),

path(
    'movie/<int:movie_id>/remove-favorite/',
    views.remove_favorite,
    name='remove_favorite'),

path(
    'favorites/',
    views.my_favorites,
    name='favorites'),

path(
    'comment/<int:comment_id>/edit/',
    views.edit_comment,
    name='edit_comment'
),

path(
    'comment/<int:comment_id>/delete/',
    views.delete_comment,
    name='delete_comment'
),
]