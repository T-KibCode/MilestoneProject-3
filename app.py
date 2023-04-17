from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://api.themoviedb.org/3/movie/550?api_key=9ee4a43299a1ad44c8b7db387a6ee72b"
    response = requests.get(url)
    data = response.json()["results"][:3] ## Testing to attempt to limit called responses to 3 title cards for Caroseul
    for movie in data:
        movie["poster_path"] = "https://image.tmdb.org/t/p/w500" + movie["poster_path"]
        movie["vote_average"] = int(movie["vote_average"] * 10) ## Attempt to convert call back answer in to a percentage for visual representation.
    return render_template("index.html", movies=data)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/search")
def search():
    return render_template("search.html")



if __name__ == "__main__":
    app.run(debug=True)