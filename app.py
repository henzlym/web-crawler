from flask import Flask, jsonify, request
from newspaper import Article
import json
import feedparser
import re
from flask_cors import CORS
from urllib.parse import urlparse

app = Flask(__name__)

def strip_tags(description):
    return re.sub('<[^<]+?>', '', description)
    
def get_domain_name(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    domain_name = hostname.split('.')[-2] + '.' + hostname.split('.')[-1]
    return domain_name
    
def is_valid_url(feed_url):
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )
    if feed_url == '':
        return False
    if not re.match(url_pattern, feed_url):
        return False
    return True
    
@app.route("/")
def index():
    return "Hello World!"
    
    
if __name__ == '__main__': app.run(debug=True)