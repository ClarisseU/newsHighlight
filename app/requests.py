import urllib.request,json
from .models import News

#Getting api key
api_key = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=NEWS_API_KEY'

#Getting the news base url
base_url = 'https://newsapi.org/v2/sources?apiKey=NEWS_API_BASE_KEY'

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_KEY']

