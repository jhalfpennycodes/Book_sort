import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Flask settings
SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'

# Flask-SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True # Avoids SQLAlchemy warning

# Flask-User settings
USER_APP_NAME = "BookSort"
USER_ENABLE_EMAIL = False
USER_ENABLE_USERNAME = True
USER_REQUIRE_RETYPE_PASSWORD = False
USER_ENABLE_REMEMBER_ME = True