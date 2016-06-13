from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, ValidationError
from wtforms import validators, StringField, PasswordField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import EmailField
from blog.models import Category
from author.models import Author
from chef_browser import db
from util.validators import Unique

class SetupForm(Form):
    name = StringField('Blog Name', [
            validators.Required(),
            validators.Length(max=80)
        ])
    fullname = StringField('Full Name', [validators.Required()])
    email = EmailField('Email address', [validators.DataRequired(), 
                                         validators.Email() ,
                                         Unique(Author,Author.email,message='There is already an account with that email.')])
                                                
            
            
    username = StringField('Username', [
            validators.Required(),
            validators.Length(min=4, max=25),
            Unique(Author,Author.username,message='There is already an account with that username.')])
    #Unique(Author, Author.email, message='There is already an account with that email.'])
    #def validate_username(self, field):
        # count the number of user ids for that username
        # if it's not 0, there's a user with that username already
        #if db.session.query(db.func.count(Author.id)).filter_by(username=field).scalar():
            #raise ValidationError('this username is already taken')
    
    password = PasswordField('New Password', [
            validators.Required(),
            validators.EqualTo('confirm', message='Passwords must match'),
            validators.Length(min=4, max=80)
        ])
    confirm = PasswordField('Repeat Password')

def categories():
    return Category.query

class PostForm(Form):
    image = FileField('Image', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    title = StringField('Title', [
            validators.Required(),
            validators.Length(max=80)
        ])
    body = TextAreaField('Content', validators=[validators.Required()])
    category = QuerySelectField('Category', query_factory=categories, allow_blank=True)
    new_category = StringField('New Category')