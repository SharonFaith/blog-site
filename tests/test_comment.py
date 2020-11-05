from app.models import Comment
from app import db
import unittest

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comment(comment_body = 'this is a comment', blog_id = 1)

   
    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment_body, 'this is a comment')
        self.assertEquals(self.new_comment.blog_id, 1)
        

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())> 0)

