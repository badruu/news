import unittest
from app.models import Source
# Source = source.Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behavior of source class
    '''
    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_source = Source('bloomberg','Bloomberg','bloomberg delivers business and markets news','http://www.bloomberg.com','business','en','us')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    # def test_source_instance(self):
    #     ''' 
    #     test to confirm initialization of source objects
    #     '''

    #     self.assertEquals(new_source.id,'bloomberg')
    #     self.assertEquals(new_source.id,'Bloomberg')
    #     self.assertEquals(new_source.id,'bloomberg delivers business and markets news')
    #     self.assertEquals(new_source.id,'http://www.bloomberg.com')
    #     self.assertEquals(new_source.id,'business')
    #     self.assertEquals(new_source.id,'en')
    #     self.assertEquals(new_source.id,'us')

