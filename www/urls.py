from django.conf.urls import include, url
from www import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^movie/(?P<pk>\d+)/$', views.MovieDetails.as_view(), name="movie_details"),

]
