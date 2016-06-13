from itsdangerous import URLSafeTimedSerializer

from chef_browser import app

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])