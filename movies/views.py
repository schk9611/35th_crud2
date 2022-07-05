import json

from django.http import JsonResponse
from django.views import View

from movies.models import *

class ActorsView(View):
    def get(self, request):
        actors = Actor.objects.all()
        results = []

        for actor in actors:
            my_movies = []
            movies = actor.movie_set.all()
            for movie in movies:
                my_movies.append(movie.title)
            results.append(
                {
                    "first_name" : actor.first_name,
                    "last_name" : actor.last_name,
                    "my_movie" : my_movies
                }
            )
        return JsonResponse({'results':results}, status=200)

class MoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        results = []

        for movie in movies:
            actor_list = []
            actors = movie.actors.all()
            for actor in actors:
                actor_list.append(actor.first_name)
            results.append(
                {
                    "title" : movie.title,
                     "running_time" : movie.running_time,
                     "actor_list" : actor_list
                 }
            )
        return JsonResponse({'results':results}, status=200)