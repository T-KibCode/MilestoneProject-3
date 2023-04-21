import requests
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://api.themoviedb.org/3/trending/all/day?api_key=9ee4a43299a1ad44c8b7db387a6ee72b"
    response = requests.get(url)
    data = []
    for result in response.json()["results"]:
        movie = {
            "title": result.get("title", result.get("name", "Unknown")),
            "poster_path": "https://image.tmdb.org/t/p/w500" + result.get("poster_path", ""),
            "vote_average": int(result.get("vote_average", 0) * 10)
        }
        data.append(movie)
    return render_template("index.html", movies=data)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/search")
def search():
    return render_template("search.html")



if __name__ == "__main__":
    app.run(debug=True)