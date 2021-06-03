
from flask import Flask, jsonify, render_template, request, redirect, url_for
import json 
import sys

sys.path.append(".")
from config import pgpassword
from config import aws_access_key_id, aws_secret_access_key
from sqlalchemy import create_engine
from werkzeug.utils import secure_filename
import boto3
# create a simple flask to return the HTML
app = Flask(__name__)

# a request to boto3
s3 = boto3.client(
    service_name='s3',
    region_name='ca-central-1',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Print out bucket names


app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 16
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'
# making the connection
engine = create_engine (f'postgresql://postgres:{pgpassword}@localhost:5432/PokemonTCG', echo=False)
sample_collector_number = '062/202'
pokemon_Data = None


@app.route("/", methods = ['GET','POST'])
def welcome():
    # if post request
    if request.method == 'POST':
        print(request.files)

        uploaded_file = request.files['fileToUpload']
        filename = uploaded_file.filename
        ### if want to save image:
        filename = secure_filename(uploaded_file.filename)
        # if filename == '':
        #    abort(400, 'Image has no filename')
        # use boto3 to upload image to S3
        s3.upload_fileobj(
            uploaded_file,
            "pokemon-cards-1",
            uploaded_file.filename,
            ExtraArgs={
                "ACL": "public-read",
                "ContentType": uploaded_file.content_type
            }
        )

        # get image url/uri back
        image_url = "{}{}".format("https://pokemon-cards-1.s3.ca-central-1.amazonaws.com/", uploaded_file.filename)
        print(image_url)
        # upload to Google (make request to Google API)flask run 
        #r = requests.post(google_url, params={}, json={}, headers={'Authentication': api_token})
        #rjson = r.json()
        ### process the file
        query_str = ''# getting from Google results
        # use boto3 to delete image
        return redirect(url_for('returnedCard'))
    return render_template('home page asmae.html')


@app.route("/visualization")
def returnedCard():
    ## check session maker on sqlachemy documentation
    #session = session_maker()
    #pokemon_Data = session.query(PokemonTable)\
    #                    .filter(PokemonTable.<field> == query_str)\
    #                    .first()
    #if not pokemon_Data:
    #    flash('We couldnt find your Pokemon')
    #f    return redirect(url_for('welcome'))
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
