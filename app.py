import os
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html", content="name", r=2)

if __name__ == "__name__":
    app.run()

