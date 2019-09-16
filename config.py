import os

class Config:
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=NEWS_API_BASE
    -KEY'
    NEWS_API_KEY = os.environ.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=NEWS_API_KEY')
    SECRET_KEY = os.environ.get('1234567890')
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config.options = {
    'development': DevConfig,
    'production': ProdConfig
}        