from wtforms import StringField

from ProjectMovieAPI_Flask import main_functions
import requests
from flask_wtf import FlaskForm


class MovieParameters(FlaskForm):
    moviename = StringField('title')
    movieposter = StringField('poster path')
    moviepopularity = StringField('popularity')


def moviepass(moviename):
    main_functions.save_to_file(get_movie_info(moviename), "ProjectMovieAPI_Flask/JSON_Files/movies.json")

    movies_json = main_functions.read_from_file("ProjectMovieAPI_Flask/JSON_Files/movies.json")

    movies_info = movies_json['results'][0]

    parameters = {'movies_info': movies_info,'response':"success"}
    return parameters


def get_movie_info(moviename):
    url = "https://api.themoviedb.org/3/search/movie?api_key="
    Api_key = main_functions.read_from_file("ProjectMovieAPI_Flask/JSON_Files/API.json")
    Api_key = Api_key["API"]
    url2 = url + Api_key + "&query=" + moviename
    request_json = requests.get(url2).json()
    return request_json

def singleMovie():
    main_functions.save_to_file(get_movie_info(), "ProjectMovieAPI_Flask/JSON_Files/singleMovies.json")
    url3="https://api.themoviedb.org/3/search/movie?api_key="
    Api_key = main_functions.read_from_file("ProjectMovieAPI_Flask/JSON_Files/API.json")

    Api_key = Api_key["API"]
    url4=url3+Api_key+"&query=" +"Blade"
    request_json =requests.get(url4).json()
    main_functions.save_to_file(request_json, "singleMovies.json")
    movies = main_functions.read_from_file("singleMovies.json")

    mymovies = movies['results']

    for i, film in enumerate(mymovies):
        if film['title']==str("Blade"):
            print(film['id'])
            movieID = film['id']
            return movieID









