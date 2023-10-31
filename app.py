from flask import Flask, render_template
import requests
import json

API = 'https://adsbexchange-com1.p.rapidapi.com/v2/lat/27.943721/lon/-82.537932/dist/5/'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    req = requests.get(API)
    data = req.content
    print(req.content)
    return render_template('index.html', data= data)

