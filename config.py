import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Flask settings
SECRET_KEY = 'sCyrqNg9tH#cH5fYkr^jmWM!H9te&vvaw^Mf337LG8KE66XoDhLj5poEyyd26hb' \
             'ELa9n7QUQ@HVB^bL@ougD55K&iNe@BbZ8qEi2ns4ZbT#Y9Fe4vNN%E%Te!Szi7#oq'

# Flask-SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True # Avoids SQLAlchemy warning

# Flask-User settings
USER_APP_NAME = "BookSort"
USER_ENABLE_EMAIL = False
USER_ENABLE_USERNAME = True
USER_REQUIRE_RETYPE_PASSWORD = False
USER_ENABLE_REMEMBER_ME = True