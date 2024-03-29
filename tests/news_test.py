import unittest
from app.models import News, Source

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''


        self.new_news = News('Fox','crazy','The Amazing Lion','A lion that saves a gazelle from an alligator','https://i.kinja-img.com/gawker-media/image/upload/s--H8pqYMUW--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/ug34lxszlekl8efydtj3.png','image','30/06/2019')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))



# Test class source
class SourceTest(unittest.TestCase):
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''


        self.new_source = Source('Fox','crazy','A lion that saves a gazelle from an alligator','https://i.kinja-img.com/gawker-media/image/upload/s--H8pqYMUW--/c_fill,fl_progressive,g_center,h_900,q_80,w_1600/ug34lxszlekl8efydtj3.png','image','30/06/2019')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))






