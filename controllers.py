from flask import render_template

from app import app
from models import Movie, Producer

@app.route('/movie/<int:id>')
def movie(id):
    movie = Movie.query.filter_by(id=id).first()
    if movie:
        producer = Producer.query.filter_by(id=movie.producer_id).first()
        return render_template('movie.html', movie=movie, producer=producer)
    else:
        return 'Film yoxdur!'


@app.route('/movies/')
def movies():
    movies = Movie.query.filter_by(status=True).all()
    if movies:
        return render_template('movies.html', movies=movies)
    else:
        return 'Filmler yoxdur!'


