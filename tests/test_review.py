import unittest
from app.models import Articles, Sources

class ArticleTest(unittest.TestCase):
    '''
    a class test to check the behaviur of the article
    '''
    def setUp(self):
       '''
       set up method that run before every test
       '''
       self.new_article= Articles('Jennings Brown','What to Do When You Receive','On Monday, YouTube filed a lawsuit against one of its users for  extorting others','https://gizmodo.com/man-claims-he-invented-bitcoin-is-ordered-to-pay-billi-1837659816','https://i.kinja-img.com/gawker-media/image/upload/s--H8pqYMUW--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/ug34lxszlekl8efydtj3.png','2019-08-21T20:31:00Z')
   
    def tearDown(self):
        Articles.article_list = []
            
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))
    
    def test_init(self):
        self.assertEqual(self.new_article.author,"Jennings Brown")
        self.assertEqual(self.new_article.title,"What to Do When You Receive")
        
        self.assertEqual(self.new_article.description,"On Monday, YouTube filed a lawsuit against one of its users for  extorting others")
        self.assertEqual(self.new_article.url,"https://gizmodo.com/man-claims-he-invented-bitcoin-is-ordered-to-pay-billi-1837659816") 
        self.assertEqual(self.new_article.urlToImage,"https://i.kinja-img.com/gawker-media/image/upload/s--H8pqYMUW--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/ug34lxszlekl8efydtj3.png")
        self.assertEqual(self.new_article.publishedAt,"2019-08-21T20:31:00Z")
      
      
# if __name__ == '__main__':
    # unittest.main()           

            