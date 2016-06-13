import os 
SECRET_KEY = 'you-will-never-guess'
DEBUG=True
DB_USERNAME = 'maliksjsu'
DB_PASSWORD = ''
BLOG_DATABASE_NAME = 'cb'
DB_HOST=os.getenv('IP', '0.0.0.0')
DB_URI = "mysql+pymysql://%s:%s@%s/%s" % (DB_USERNAME, DB_PASSWORD, DB_HOST, BLOG_DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
#SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@mysql:3306/%s' % (DB_USERNAME, DB_PASSWORD, BLOG_DATABASE_NAME)
UPLOADED_IMAGES_DEST = '/home/ubuntu/workspace/flask_init/chef_browser/static/images'
UPLOADED_IMAGES_URL = '/static/images/'
FACEBOOK_APP_ID = '1176702149047151'
FACEBOOK_APP_SECRET = 'e4477848b86afc253f63ea0bbe14e37b'
OAUTH_CREDENTIALS= {
    'facebook': {
        'id': '1176702149047151',
        'secret': 'e4477848b86afc253f63ea0bbe14e37b'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}
FB_CLIENT_ID = '1176702149047151'
FB_CLIENT_SECRET = 'e4477848b86afc253f63ea0bbe14e37b'

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
#MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
#MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

MAIL_USERNAME = 'djminusone@gmail.com'
MAIL_PASSWORD = '0581109007'

# administrator list
ADMINS = ['djminusone@gmail.com']