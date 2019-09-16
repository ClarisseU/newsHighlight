class Sources:
    '''
    Source class to define sources Objects
    '''
    
    def __init__(self,author,title,imageurl,description,url):
        self.author = author
        self.title = title
        self.imageurl = imageurl
        self.description = description
        self.url = url
        
class Articles:
    '''
    Articles class define articles objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
            
        
class Review:
    
    all_reviews = []
    
    def __init__(self,news_id,title,review):
        self.news_id = news_id
        self.title = title
        self.review = review
        
    def save_review(self):
        Review.all_reviews.append(self)
        
    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
        
    @classmethod
    def get_reviews(cls,id):
        response = []
         
        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)
                
        return response
    
                             