from flask import render_template, request,redirect,url_for
from . import main
from ..requests import get_source, get_articles
from ..models import Review,Articles,Sources

#Views
@main.route('/')
def index():
    '''
    View root page function which returns the index page and its data
    '''
    #getting sources
    news_sources = get_source('entertainment')
    news_sources1 = get_source('sports')
    news_sources2 = get_source('business')
    print(news_sources)
    title = 'Home - Welcome to the news website'
    
    return render_template('index.html', title = title, news_sources = news_sources, news_sources1= news_sources1, news_sources2 = news_sources2)
    
    
@main.route('/everything/<source_id>') 
def source(source_id):
    '''
    Function to view  the source page and it returns the article page
    '''
    news_articles = get_articles(source_id)
    print(news_articles)
    
    title = 'Article - Welcome to articles'
    return render_template('articles.html',id = source_id, title = title, article= news_articles)  