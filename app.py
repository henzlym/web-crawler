from flask import Flask, jsonify, request
from newspaper import Article
import json
import feedparser
import re
from flask_cors import CORS
from urllib.parse import urlparse

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"
    
    
if __name__ == '__main__': app.run(debug=True)