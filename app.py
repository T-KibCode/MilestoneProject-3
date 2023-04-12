import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__name__":
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=True
	)

# import requests
# import moviecreds

# https://developers.themoviedb.org/ - Documentation #

# url ="https://api.themoviedb.org/3/authentication/token/new?api_key=9ee4a43299a1ad44c8b7db387a6ee72b"

# querystring = {"q":"game of thr"}

#headers = {
#	"X-RapidAPI-Key": "ad2be7f88amshb389857c019ff11p12d386jsn9fa9dc12feb9",
#	"X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
#}

#response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)