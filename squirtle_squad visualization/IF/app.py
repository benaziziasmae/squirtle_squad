from flask import Flask, jsonify, render_template
import json
import sys
sys.path.append(".")
from config import tcgapikey, pgpassword
from sqlalchemy import create_engine




# create a simple falsk to return the HTML
app = Flask(__name__)

# making the connection
engine = create_engine('postgresql://postgres:{pgpassword}@localhost:5432/PokemonTCG', echo=False)
sample_collector_number = '062/202'
pokemon_Data = None

@app.route("/")
def welcome(): 
    
    # on submission of image (WIP)

    # run machine learning to identify query (result = output variable) (WIP)

    
    ## Do stuff with database connection (run query)
    
    # query engine with result (use sample_collector_number for now)

    # assign global? varaible or pass directly to new html
    
    return render_template("home.html")

@app.route("/visualization")
def returnedCard():

    
    pokemon_Data = {
        "id":"swsh35-2",
        "name":"Weedle",
        "number":"002\/073",
        "legalities":
            {"unlimited":"Legal","standard":"Legal","expanded":"Legal"},
        "images":{
            "small":"https:\/\/images.pokemontcg.io\/swsh35\/2.png",
            "large":"https:\/\/images.pokemontcg.io\/swsh35\/2_hires.png"},
        "prices":{
            "reverseHolofoil":
                {"low":0.05,"mid":0.29,"high":1.37,"market":0.24},
            "normal":
                {"low":0.01,"mid":0.13,"high":1.0,"market":0.07}},
        "set_id":"swsh35",
        "set_name":"Champion's Path",
        "date":1622239842548}

    

    return render_template("visualization.html", card_data=pokemon_Data)



