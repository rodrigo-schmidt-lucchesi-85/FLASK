from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# This extension manages the user logged-in state, so that for example users 
# can log in to the application and then navigate to different pages while 
# the application "remembers" that the user is logged in.


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
migrate = Migrate(app, db)

from app import routes
