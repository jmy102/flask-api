from flask import Flask, render_template
from flask import request
import requests

app = Flask(__name__)

# establish the home route
@app.route('/', methods = ["GET", "POST"])
def index():
    # data scrape
    apikey = ""
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto"+"?apikeyu="+apikey)
    # transform data
    data = response.json()
    img = data["sprites"]["front_default"]
    name = data["name"]
    return render_template("index.html", poke_src = img, name = name)

if __name__ == "__main__":
    app.run()