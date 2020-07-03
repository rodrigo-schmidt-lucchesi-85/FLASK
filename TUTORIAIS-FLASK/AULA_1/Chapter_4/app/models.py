from app import db
# We're using SQLAlchemy to handle the database creation, 
# a class-based approach to an SQLite database.  
# Four fields are generated, to handle the user login app.

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
