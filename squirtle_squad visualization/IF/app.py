from flask import (
    Flask, jsonify, render_template, request, redirect, url_for, flash, abort
)
import json
import sys
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .GoogleVisionApi import run_model, UnableToDecodeImageError

from .config import pgpassword, secret_key, SQLALCHEMY_DATABASE_URI
from .config import aws_access_key_id, aws_secret_access_key, bucket_url,bucket_name
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData, Table
from sqlalchemy.orm import sessionmaker, Session
from werkzeug.utils import secure_filename
import boto3
from sqlalchemy.ext.automap import automap_base
from urllib.parse import urlencode, quote_plus, unquote

# create a simple flask to return the HTML
app = Flask(__name__)
app.secret_key = secret_key
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 16
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

### initialize the db connection
db = SQLAlchemy()
db.init_app(app)

### set config to boto3 client
s3 = boto3.client(
    service_name='s3',
    region_name='ca-central-1',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

SAMPLE_COLLECTOR_NUMBER = '062/202'
POKEMON_DATA = None

@app.route("/", methods = ['GET','POST'])
def welcome():

    if request.method == 'POST':

        uploaded_file = request.files['fileToUpload']
        filename = uploaded_file.filename

        ### make sure the filename is secure
        filename = secure_filename(uploaded_file.filename)
        if filename == '':
           flash('No image was uploaded. Showing sample', 'danger')
           return render_template('home page asmae.html')

        ### use boto3 to upload image to S3
        s3.upload_fileobj(
            uploaded_file,
            "pokemon-cards-1",
            uploaded_file.filename,
            ExtraArgs={
                "ACL": "public-read",
                "ContentType": uploaded_file.content_type
            }
        )
        image_url = "{}{}".format(f"https://{bucket_url}/", filename)

        ### upload to Google API Vision (make request to Google API)flask run
        try:
            query_str = run_model(image_url)
            query_str = query_str.replace('/','%2f') # quote_plus(query_str)
        except UnableToDecodeImageError:
            # on error, delete image and render home page
            delete_res = s3.delete_object(Bucket=bucket_name, Key=image_url)
            flash('Could not read image, please try again!', 'danger')
            return render_template('home page asmae.html')

        delete_res = s3.delete_object(Bucket=bucket_name, Key=image_url)
        # redirect to card to display
        return redirect(url_for('returnedCard', query_str=query_str))

    return render_template('home page asmae.html')

@app.route("/visualization")
@app.route("/visualization/<query_str>")
def returnedCard(query_str=''):

    query_str = query_str.replace('%2f','/') or SAMPLE_COLLECTOR_NUMBER
    # query_str = unquote(query_str) or SAMPLE_COLLECTOR_NUMBER
    metadata = MetaData()
    SwShSeries = Table('SwShSeries', metadata, autoload=True, autoload_with=db.engine)

    result = db.session.query(SwShSeries)\
                        .filter(SwShSeries.c.number == SAMPLE_COLLECTOR_NUMBER)\
                        .first()
    if not result:
        flash('We couldnt find your Pokemon in our db', 'danger')
        return redirect(url_for('welcome'))

    pokemon_Data = {
        "id":result.id,
        "name":result.name,
        "number":result.number,
        "legalities": result.legalities,
        "images":result.images,
        "prices": result.prices,
        "set_id":result.set_id,
        "set_name":result.set_name,
        "date": datetime.strftime(result.date,'%Y-%m-%d')
    }
    return render_template("visualization.html", card_data=pokemon_Data)


