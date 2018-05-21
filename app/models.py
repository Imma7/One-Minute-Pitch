from . import db

class User(db.Model): #create 'User' class to help in creating new users
   
    __tablename__ = 'users' #__tablename__ variable allows us to give the tables in our db proper names
    id = db.Column(db.Integer,primary_key = True) #create columns using db.Column class which represents a single column.db.Integer specifies data to be stored
    username = db.Column(db.String(255)) #db.String class specifies data to be a string with 255 characters maximum
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __repr__(self): #repr method easens debugging of our application
        return f'User {self.username}'

class Pitch(db.Model):
    #List of pitches

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    comment = db.Column(db.String)
    category = db.Column(db.String)
    user_id = db.Column(db.String, db.ForeignKey('user.id'))
    vote = db.Column(db.Integer)


class Comment(db.Model):
    #User comments

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    feedback = db.column(db.String)
    user_id = db.Column(db.String(255), db.ForeignKey('user.id'))
    time_posted = db.Column(db.dateTime)
