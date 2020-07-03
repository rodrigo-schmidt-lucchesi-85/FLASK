from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

# In the model's table, we're creating three functions: __repr__() a way to 
# represent the object on the database, which username is the field chosen; 
# set_password() to generate an encrypted password to be inserted on the User 
# table; check_password() to compare the hashed and string type password for 
# validation purposes. Finally, using a decorator to add a query method to the 
# LoginManager extension loading the user id to handle the state inside the 
# application.



class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
