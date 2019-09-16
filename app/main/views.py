from flask import render_template, request,redirect,url_for
from . import main
from ..requests import get_news, get_new, search_new
from .forms import ReviewForm
from ..models import Review

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
    
    return render_template('index.html', title = title, news = news_sources, news1= news_sources1, news2 = news_sources2)
    
    
@main.route('/everything/<source_id>') 
def source(source_id):
    '''
    Function to view  the source page and it returns the article page
    '''
    news_articles = get_article(source_id)
    
    title = 'Article - Welcome to articles'
    return render_template('articles.html',id = source_id, title = title, article= news_articles)  