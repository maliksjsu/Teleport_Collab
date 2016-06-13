from chef_browser import app, db
from flask import render_template, redirect, session, request, url_for, flash
from user.form import RegisterForm, LoginForm
from user.models import User
#from flask_oauth import OAuth
import bcrypt
from rauth.service import OAuth2Service
'''
from flask_sqlalchemy import SQLAlchemy
app.config.from_object(__name__)
SQLALCHEMY_DATABASE_URI = 'sqlite:///facebook.db'
SECRET_KEY = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'
db1 = SQLAlchemy(app)
'''
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user,\
    current_user
from oauth import OAuthSignIn
'''
class User1(db1.Model):
    id = db1.Column(db.Integer, primary_key=True)
    username = db1.Column(db.String(80), unique=True)
    fb_id = db1.Column(db.String(120))

    def __init__(self, username, fb_id):
        self.username = username
        self.fb_id = fb_id

    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def get_or_create(username, fb_id):
        user = User1.query.filter_by(username=username).first()
        if user is None:
            user = User1(username, fb_id)
            db1.session.add(user)
            db1.session.commit()
        return user
'''
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '1176702149047151',
        'secret': 'e4477848b86afc253f63ea0bbe14e37b'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}


lm = LoginManager(app)
lm.login_view = 'index'
'''
facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=app.config['FACEBOOK_APP_ID'],
    consumer_secret=app.config['FACEBOOK_APP_SECRET'],
    request_token_params={'scope': 'email'}
)
'''


@app.route('/')
def init():
    return redirect(url_for('login'))

@app.route('/index')
def index():
    return render_template('frontend/one-page.html')

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
    
@app.route('/loginfb', methods=('GET', 'POST'))
def loginfb():
    return render_template('user/index.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    error = None

    if form.validate_on_submit():

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        user = User(
            fullname=form.fullname.data,
            email=form.email.data,
            username=form.username.data,
            password=hashed_password,
            is_author=True,
            nickname=None,
            social_id=None
        )
        db.session.add(user)
        db.session.flush()

        if user.id:
            flash("User Created")
            db.session.commit()

        else:
            db.session.rollback()
            error = "Error registering User"

        return redirect('index')

    return render_template('user/register.html', form=form, error=error)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None

    if session.get('username'):
        #login_user(session.get('username'), True)

        username = session.get('username')
        #user = User.query.filter_by(username=username)
        #login_user(username, True)
        flash('You are already logged in as %s' % username)
        return redirect(url_for('index'))

    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)

    if form.validate_on_submit():
        user = User.query.filter_by(
            username=form.username.data
        ).first()

        if user:

            if bcrypt.hashpw(form.password.data, user.password) == user.password:
                session['username'] = form.username.data
                session['is_author'] = user.is_author

                if 'next' in session:

                    next = session.get('next')
                    session.pop('next')

                    return redirect(next)

                else:

                    return redirect(url_for('index'))
            else:
                error = 'Incorrect Password'
        else:
            error = "Incorrect Username"

    return render_template('user/login.html', form=form, error=error)

'''
@app.route('/index')
def index():
    if session.get('username'):
        fullname = session.get('fullname')
        user = User.query.filter_by(fullname=fullname).first()
        login_user(user, True)
        return render_template('user/index.html')

    return render_template('user/index.html')
'''



@app.route('/logout')
def logout():

    try:
        logout_user()
        session.pop('username')
    except:
        pass

    return render_template('user/index.html')



@app.route('/success')
def success():
    form = RegisterForm()
    flash(form.fullname.data)
    return render_template('user/index.html')

@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('index'))
    user = User.query.filter_by(social_id=social_id).first()


    if not user:
        user = User(social_id=social_id, nickname=username, email=email, fullname=username, password=None, username=username)

        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('index'))




