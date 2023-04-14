from flask import Flask, render_template
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("app.py"),
    autoescape=select_autoescape()
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(
        host=("IP","0.0.0.0"),
        port=int("PORT","5000"),
        debug=True
    )

