from flask import Flask, jsonify, render_template
import json
import sys
sys.path.append(".")
from config import tcgapikey, pgpassword
from sqlalchemy import create_engine
import requests



# create a simple falsk to return the HTML
app = Flask(__name__)

# making the connection
engine = create_engine('postgresql://postgres:{pgpassword}@localhost:5432/PokemonTCG', echo=False)
sample_collector_number = '062/202'


@app.route("/", methods=['GET','POST'])
def welcome():

    # if post request
    if requests.method == 'POST':

        uploaded_file = request.files['file']
        filename = uploaded_file.filename

        ### if want to save image:
        # filename = secure_filename(uploaded_file.filename)
        # if filename == '':
        #    abort(400, 'image has no filename')

        ### use boto3 to image upload image to s3   
        
        #request to boto3
        

        # get image url/uri back
        image_url = # get image url from boto3 request

        #upload to google (make request to google api)
        r = requests.post(google url, parameters = {}, json={}, headers{authentication: api_token})    

        rjson = r.json()

        
        ### request for image uploaded to be deleted
        

        ### process the file

        query_str = # getting from google results

        return redirect(url_for('returnedCard', query_str = query_str))

    return render_template('home.html')

@app.route("/visualization/<str:query_str>")

def returnedCard(query_str = None):

    #separate sessions if there are multiple people using at once; 
    ## flask-sqlalchemy
    session = session_maker()

    pokemon_Data = session.query('pgadminTableName').filter(pokemontable.field == query_str).first()
    
    if not pokemon_Data:
        flash('We couldnt your card')
        abort(404, 'not found')
    # run query > return data
    
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



