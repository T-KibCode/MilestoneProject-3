import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello! this is the main page" 

if __name__ == "__name__":
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=True)



