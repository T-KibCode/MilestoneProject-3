from FlickFanatic.models import Movie, Actor

@app.route("/movies", methods=['GET'])
def movies():
    movies = Movie.query.all()
    return render_template('movies.html', movies=movies)

@app.route("/actors", methods=['GET'])
def actors():
    actors = Actor.query.all()
    return render_template('actors.html', actors=actors)
