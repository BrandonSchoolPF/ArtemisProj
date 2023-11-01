from flask import Flask, render_template, jsonify
import requests
import json
from api import *
from flask_compress import Compress

app = Flask(__name__)



@app.route("/")
@app.route('/index')
def index():
    API_Add = 'https://adsbexchange-com1.p.rapidapi.com/v2/lat/27.943721/lon/-82.537932/dist/5/'
    headers = {	"X-RapidAPI-Key" : "INSERT KEY",	"X-RapidAPI-Host" : "adsbexchange-com1.p.rapidapi.com"}
    response = requests.get(API_Add, headers=headers)
    
    if response.status_code != 200: 
        print("Call did not work")
    else: 
        data = response.json()
        return jsonify(data)
        

if __name__ == '__main__':
    app.run(debug=True)
