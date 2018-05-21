from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model): #create 'User' class to help in creating new users
   
    __tablename__ = 'users' #__tablename__ variable allows us to give the tables in our db proper names
    id = db.Column(db.Integer,primary_key = True) #create columns using db.Column class which represents a single column.db.Integer specifies data to be stored
    username = db.Column(db.String(255)) #db.String class specifies data to be a string with 255 characters maximum
    email = db.Column(db.String)
    password_hash = db.Column(db.String)
    pass_secure = db.Column(db.String(255))


    pass_secure  = db.Column(db.String(255))

        @property #@property decorator creates a write only class property 'password'
        def password(self):
            raise AttributeError('You cannot read the password attribute')

        @password.setter
        def password(self, password):
            self.pass_secure = generate_password_hash(password)


        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self): #repr method easens debugging of our application
        return f'User {self.username}'


class Pitch(db.Model):
    #List of pitches

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    comment = db.Column(db.String)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    vote = db.Column(db.Integer)
    users = db.relationship('User', backref='pitch', lazy='dynamic')


class Comment(db.Model):
    #User comments

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    feedback = db.column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time_posted = db.Column(db.DateTime)
    pitches = db.relationship('Pitch', backref='comment', lazy='dynamic')