import unittest
from models import article
Article=article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behavior of the article class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''

        self.new_article=Article('wired','Wired','Michael Hardy','Trump casinos','Photographer Brian Rose turns his lens on the city','https://www.wired.com/story/trumps-casinos-could-not-make-atlantic-city-great-again/','https://media.wired.com/photos/5c911b3b33cb7721bef3230b/191:100/pass/01_BrianRose_AC.jpg','2019-03-19T16:43:21Z','Like many people, photographer and New York City resident Brian Rose was blindsided by Donald Trumps victory in the 2016 presidential election')

    def test_article(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_article_instance(self):
        '''
        to check whether article objects and initialized properly
        '''
        self.assertEquals(new_article.id,'wired')
        self.assertEquals(new_article.name,'Wired')
        self.assertEquals(new_article.author,'Michael Hardy')
        self.assertEquals(new_article.title,'Trump casinos')
        self.assertEquals(new_article.description,'Photographer Brian Rose turns his lens on the city')
        self.assertEquals(new_article.url,'https://www.wired.com/story/trumps-casinos-could-not-make-atlantic-city-great-again/')
        self.assertEquals(new_article.urlToImage,'https://media.wired.com/photos/5c911b3b33cb7721bef3230b/191:100/pass/01_BrianRose_AC.jpg')
        self.assertEquals(new_article.publishedAt,'2019-03-19T16:43:21Z')
        self.assertEquals(new_article.content,'Like many people, photographer and New York City resident Brian Rose was blindsided by Donald Trumps victory in the 2016 presidential election')

if __name__=='__main__':
    unittest.main()