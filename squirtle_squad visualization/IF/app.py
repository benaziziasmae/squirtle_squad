from flask import Flask, jsonify, render_template
import json
#create a simple falsk to return the HTML
app = Flask(__name__)

@app.route("/home")
def welcome(): 
    
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



