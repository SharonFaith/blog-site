from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, Blog, Comment
from .. import db, photos
from .forms import UpdateProfile, BlogForm

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    blogs = Blog.get_all_blogs()

    time_blogs = []

    for blog in blogs:
        time_blogs.insert(0, blog)


    return render_template('index.html', blogs = time_blogs)

@main.route('/user/<uname>', methods = ['GET', 'POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()
#    form = DeleteUser()
 
    
   
    if user is None:
        abort(404)
    
    else:

        return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    

    if user is None:
        abort(404)

    form = UpdateProfile()


    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))
    
    return render_template('profile/update.html', form = form)

@main.route('/user/<uname>/update/pic', methods  = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname = uname))


@main.route('/blog/new_post', methods = ['GET', 'POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    
    if blog_form.validate_on_submit():
        title = blog_form.title.data
        content = blog_form.content.data

        new_blogs = Blog(title = title, content = content, user = current_user)
        new_blogs.save_blog()

        return redirect(url_for('main.index'))

    return render_template('new_blog_post.html', form = blog_form)

@main.route('/blog/<blog_id>')
def one_blog(blog_id):
    blog = Blog.query.filter_by(id = blog_id).first()
    comments = Comment.get_all_comments()
    time_comment = []
    
    for comment in comments:
        if comment.blog_id == blog_id:
            time_comment.insert(0, comment)

    blogs_id = blog_id

    return render_template('blog_post.html', comments = time_comment, blog = blog)
