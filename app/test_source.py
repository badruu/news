import unittest
from models import source
Source = source.Source

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

if __name__ == '__main__':
    unittest.main()
