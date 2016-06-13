from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flaskext.markdown import Markdown
import flask_login as flask_login
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
import sendgrid



login_manager = flask_login.LoginManager()
app = Flask(__name__)

app.config.from_object('settings')
db = SQLAlchemy(app)
login_manager.init_app(app)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'djminusone@gmail.com',
    MAIL_PASSWORD = '0581109007',
))
mail = Mail(app)







# migrations
migrate = Migrate(app, db)

# markdown
md = Markdown(app, extensions=['fenced_code', 'tables'])

# images
uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)


from user import views
from blog import views
from author import views
from home import views
#from util import validators