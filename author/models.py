from chef_browser import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(35), unique=True)
    username = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(60))
    is_author = db.Column(db.Boolean)
    email_confirmed = db.Column(db.Boolean)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    
    def __init__(self, fullname, email, username, password, is_author=False, email_confirmed=False):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
        self.is_author = is_author
        self.email_confirmed = email_confirmed

    def __repr__(self):
        return '<Author %r>' % self.username
