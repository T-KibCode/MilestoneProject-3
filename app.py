import os
from flask import Flask

app = Flask(__name__)

## import requests

## url = "https://online-movie-database.p.rapidapi.com/auto-complete"

## querystring = {"q":"game of thr"}

## headers = {
	## "X-RapidAPI-Key": "ad2be7f88amshb389857c019ff11p12d386jsn9fa9dc12feb9",
	## "X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
## }

## response = requests.request("GET", url, headers=headers, params=querystring)

## print(response.text)

@app.route("/")
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug=False) ##Do not run debug = true when deployed, only when testing ##
    

