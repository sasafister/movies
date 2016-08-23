import microdata
from django.core.management.base import BaseCommand, CommandError
from urllib.request import urlopen
from bs4 import BeautifulSoup
from www.models import Movies, Movie
import json
import urllib

class Command(BaseCommand):
    help = 'Parsanje podataka'

    def handle(self, *args, **options):
        baseurl = "https://www.rottentomatoes.com"
        html_page = urlopen(baseurl + "/browse/opening/")
        soup = BeautifulSoup(html_page, "lxml")
        for movie in soup.find_all("div",{"class": "mb-movie"}):
            title = movie.find(class_="movieTitle").text
            url = movie.a.get('href')

            movie = Movies(title=title, url=url,  created_at="2013-12-01")
            try:
                if Movies.objects.filter(title=title).exists():
                    print("postoji")
                else:
                    movie.save()
            except (Movies.DoesNotExist):
                    print("No movies")

        # print(Movies.objects.filter(pk=1))
        movie = BeautifulSoup("https://www.rottentomatoes.com/m/mechanic_resurrection/", "lxml")
        data = soup.find_all(id="jsonLdSchema")
        for element in data:
          jsonObject = json.loads(element.string.strip())
          for el in jsonObject['itemListElement']:
              movie.url = el['director']['@type']
            #   movie.save()
