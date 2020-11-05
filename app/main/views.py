from flask import render_template, request, redirect, url_for, abort
from . import main

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')

@main.route('/user/<uname>', methods = ['GET', 'POST'])
def profile(uname):
    user = User.query.filter_by(username = uname).first()
#    form = DeleteUser()
 
    
   
    if user is None:
        abort(404)
    
    else:

        return render_template('profile/profile.html', user = user, delete = form, pitches = pitches)
