from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int( user_id))


#id, username, email || bio, profilepicpath, blogs = db.relationship with blog class,

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    '''
    Blog class
    '''
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#    comments = db.relationship('Comment', backref = 'pitch', lazy = 'dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.query.all()
        return blogs

class Comment(db.Model):
    '''
    Comment class
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    comment_body = db.Column(db.String)
    posted = db.Column(db.DateTime, default = datetime.utcnow)
#    blogs_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    blog_id = db.Column(db.Integer)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_comments(cls):
        comments = Comment.query.all()
        return comments