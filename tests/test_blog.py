from app.models import User, Blog
from app import db
import unittest

class BlogModelTest(unittest.TestCase):

    def setUp(self):
        self.user_Pat = User(username = 'Pat', password = 'potato', email = 'pat@ms.com')

        self.new_blog = Blog(title = 'general', content = 'this is a pitch', user = self.user_Pat)
    
    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_blog.title,'general')
        self.assertEquals(self.new_blog.content,'this is a pitch')
        self.assertEquals(self.new_blog.user,self.user_Pat)

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Blog.query.all())> 0)

