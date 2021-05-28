# import dependencies
import pandas as pd
import requests
import csv
import json
import datetime
import psycopg2
import sys
sys.path.append(".")
from config import tcgapikey, pgpassword
from sqlalchemy import create_engine, dialects
from re import search

# Initial API call & get request
url = 'https://api.pokemontcg.io/v2/cards?q=set.series:Sword%20&%20Shield&page=1'
data = requests.get(url, headers={'X-Api-Key':tcgapikey}).json()

# ERROR TO FIX:     "Can't connect to HTTPS URL because the SSL module is not available."

'''
# loop to get all pages of query
query_results = True
i = 2
while query_results:
    url = 'https://api.pokemontcg.io/v2/cards?q=set.series:Sword%20&%20Shield&page='+str(i)
    card_info = requests.get(url, headers={'X-Api-Key':tcgapikey}).json()
    data['data'] = data['data']+card_info['data']
    data['count'] = data['count']+card_info['count']
    print(f'Appended page {i}')
    i += 1
    if card_info['count']==card_info['pageSize']: 
        continue
    else:
        query_results= False

del data['page']
del data['pageSize']

# for each entry, split data from set dictionary
for i in range(len(data['data'])):
    try:
        data['data'][i]['prices']=data['data'][i]['tcgplayer']['prices']
    except KeyError:
        data['data'][i]['prices'] = None
    
# set info
    #set_id
    try:    
        data['data'][i]['set_id']=data['data'][i]['set']['id']
    except KeyError:
        data['data'][i]['set_id']= None

    #set_name
    try:    
        data['data'][i]['set_name']=data['data'][i]['set']['name']
    except KeyError:
        data['data'][i]['set_name']= None

    #add timestamp
    data['data'][i]['date']= datetime.datetime.now()

# collector data
    if search ('\D', data['data'][i]['number']):
        data['data'][i]['number'] = data['data'][i]['number']
    else:
        data['data'][i]['number'] = str(data['data'][i]['number']).zfill(3) + "/" + str(data['data'][i]['set']['printedTotal']).zfill(3)

# create data frame & drop unneeded information
data_clean_df = pd.DataFrame(data['data']).drop(
    columns=[
        'supertype',
        'subtypes',
        'hp',
        'rules',
        'attacks',
        'weaknesses',
        'retreatCost',
        'convertedRetreatCost',
        'artist',
        'rarity',
        'nationalPokedexNumbers',
        'evolvesTo',
        'flavorText',
        'evolvesFrom',
        'abilities',
        'resistances',
        'types',
        'tcgplayer',
        'set'])

# link to the database & create engine
engine = create_engine(f'postgresql://postgres:{pgpassword}@localhost:5432/PokemonTCG', echo=False)

# load into database with format
data_clean_df.to_sql(
    'SwShSeries',
    con=engine,
    if_exists='append',
    index=False,
    dtype={
    'legalities':dialects.postgresql.JSON,
    'images':dialects.postgresql.JSON,
    'prices':dialects.postgresql.JSON}
    )

# export as csv for local test
data_clean_df.to_csv(f'SwShSeries_{datetime.date.today()}.csv', index = False)
'''