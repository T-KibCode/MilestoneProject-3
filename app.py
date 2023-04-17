import requests
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://api.themoviedb.org/3/movie/550?api_key=9ee4a43299a1ad44c8b7db387a6ee72b"
    response = requests.get(url)
    data = [{"title": response.json()["title"],
        "poster_path": "https://image.tmdb.org/t/p/w500" + response.json()["poster_path"],
        "vote_average": int(response.json()["vote_average"] * 10)}]
    return render_template("index.html", movies=data)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/search")
def search():
    return render_template("search.html")



if __name__ == "__main__":
    app.run(debug=True)