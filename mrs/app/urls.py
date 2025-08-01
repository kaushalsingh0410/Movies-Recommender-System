from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('genre-movies/',views.genre_movies_ajax,name ='genre_movies'),
    path('movies-details/<int:id>',views.movies_details,name ='movies_details'),
    path('search/',views.search,name ='search'),
    path('search/<slug:key>/',views.search,name ='search_ksy'),
    path('videos/<int:id>/',views.videos,name ='videos'),
    path('backdrops/<int:id>/',views.backdrops,name ='backdrops'),
    path('posters/<int:id>/',views.posters,name ='posters'),
    path('credits/<int:id>/',views.credits,name ='credits'),
]