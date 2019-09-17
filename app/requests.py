import urllib.request,json
from .models import Sources, Articles
from datetime import datetime

#Getting api key
api_key = None
#Getting the news base url
article_url = None
source_url = None

def configure_request(app):
    global api_key,base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']
    articles_url = app.config['NEWS_ARTICLES_BASE_URL']
    
def get_source(category):
    '''
    function that gets the json response to our url request
    '''
    get_source_url = source_url.format(category,api_key)
    print(get_source_url)
    
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        
        sources_result = None
        
        if get_source_response['sources']:
            sources_results_list = get_source_response['sources']
            sources_result = process_sources(sources_results_list)
            
    return sources_result  

def process_sources(sources_list):
    '''
    Function that checks the news results and turn them into objects
    
    Args:
        sources_list: A list of dictionaries that contain sources details
    '''
    sources_result = []
    
    for source_item in sources_list:
        author = source_item.get('author')
        title = source_item.get('title')
        imageurl = source_item.get('urltoimage')
        description = source_item.get('description')
        url =       source_item.get('url')
        
        sources_object = Sources(author, title,imageurl,description,url)
        sources_result.append(sources_object)
        
    return sources_result

def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = articles_url.format(id,api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        articles_result = json.loads(url.read())
        
        articles_object = None
        if articles_result['articles']:
            articles_object = process_articles(articles_result['articles'])
            
    return articles_object

def process_articles(articles_list):
    '''
    function that checks the articles and processes them into instances
    '''
    articles_object = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')
        
        if image:
            articles_result = Articles(author,title,description,url,image,date)
            articles_object.append(articles_result)
            
            
    return articles_object        
        
    
    

