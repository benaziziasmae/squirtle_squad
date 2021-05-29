from flask import Flask, jsonify, render_template
import json
#create a simple falsk to return the HTML
app = Flask(__name__)


@app.route("/")

def Weclome():
    
    return render_template("index.html")









@app.route("/visualization")
def scanned(): 
    with open("pokemon_set.json", "r") as file:
        pokemon_Data = json.loads(file)
    pokemon_Data = {"name": "Weedle",
        "number":2,
        "legalities":{'unlimited': 'Legal', 'standard': 'Legal', 'expanded': 'Legal'},
        "images":{'small': 'https://images.pokemontcg.io/swsh35/2.png', 'large': 'https://images.pokemontcg.io/swsh35/2_hires.png'},
        "prices":{'reverseHolofoil': {'low': 0.05, 'mid': 0.29, 'high': 1.37, 'market': 0.24, 'directLow': 0.14}, 'normal': {'low': 0.01, 'mid': 0.13, 'high': 1.0, 'market': 0.07, 'directLow': 0.05}},
        "set_id":"swsh35",
        "set_name":"Champion's Path",
        "cards_in_set":73,
        "printed_total":80,
        "date":"2021-05-25 19:48:31.019611",

        }
    return render_template("visualization.html",pokemon_Data=pokemon_Data)



