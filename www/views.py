from django.shortcuts import render
from .models import Movies, Movie
from django.views import generic

# Create your views here.
# def index(request):
#     movies = Movies.objects.all()
#     return render(request, 'www/index.html')

class IndexView(generic.ListView):
	template_name = 'www/index.html'
	context_object_name = 'movies'

	def get_queryset(self):
		return Movies.objects.all()

class MovieDetails(generic.DetailView):
	model = Movies
	context_object_name = "obj"
	template_name = "www/movie_details.html"
