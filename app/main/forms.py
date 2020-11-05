from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required, Length

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Blog title', validators=[Required()])
    content = TextAreaField('Blog content', validators=[Required()])
    submit = SubmitField('Submit')

class NewComment(FlaskForm):
    comment = TextAreaField('New Comment', validators=[Required()])
    submit = SubmitField('Submit')