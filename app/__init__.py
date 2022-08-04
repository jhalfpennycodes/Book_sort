import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_user import UserManager
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

login_manager = LoginManager()
login_manager.login_view = 'app.login'
login_manager.init_app(app)

logging.basicConfig(filename='web-app.log', encoding='utf-8', level=logging.DEBUG)


from app.models import User

user_manager = UserManager(app, db, User)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


from app import views, models