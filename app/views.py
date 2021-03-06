from flask import render_template
from app import app

# my view functions starts from here
# decorator
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title=title)

#view function that returns the movies
# @app.route('/movie/<movie_id')
# def movie(movie_id):
#     '''
#     view function that returns the movies data
#     '''
#     return render_template('movie.html',id=movie_id)
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    view function that returns the movie data
    '''
    return render_template('movie.html',id=movie_id)
