from flask import Flask, render_template, jsonify
from flask import Flask, render_template, jsonify
import requests
import json
from api import *
from flask_compress import Compress

app = Flask(__name__)



@app.route("/")
@app.route('/index')
def index():
    req = requests.get(API)
    data = req.content
    print(req.content)
    return render_template('index.html', data= data)

