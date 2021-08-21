import os
from ProjectMovieAPI_Flask import routes, app, forms
from flask import request, render_template, url_for


@app.route('/')
@app.route('/search', methods=['GET', 'POST'])
def search():
    search_form = forms.MovieParameters(request.form)
    if request.method == 'POST':
        moviename = request.form['moviename']
        movie = forms.moviepass(moviename)
       # if movie['response'] == "error":
            #return render_template("parameter_error.html", form=search, result=movie, moviename=moviename)
        return render_template("parameter_result.html", form=search_form, result=movie, moviename=moviename,
                               title=moviename)
    return render_template("parameter_search.html", form=search_form)
