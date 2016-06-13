from chef_browser import db, app, login_manager
from flask.ext.login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(35), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(60))
    is_author = db.Column(db.Boolean)

    social_id = db.Column(db.String(64), nullable=True, unique=True)
    nickname = db.Column(db.String(64))

    #posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def __init__(self, fullname, email, username, password, social_id, nickname, is_author=False):

        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
        self.is_author = is_author

        self.social_id = social_id
        self.nickname = nickname

    def __repr__(self):
        return '<User %r>' % self.username

    @staticmethod
    def get_or_create(username, fb_id):
        user = User.query.filter_by(username=username).first()
        if user is None:
            user = User(username, fb_id)
            db.session.add(user)
            db.session.commit()
        return user
@login_manager.user_loader
def get_user(ident):
  return User.query.get(int(ident))

app.config['SECURITY_POST_LOGIN'] = '/profile'