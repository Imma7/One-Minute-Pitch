from . import db 

class User(db.Model): #create 'User' class to help in creating new users
    __tablename__ = 'users' #__tablename__ variable allows us to give the tables in our db proper names
    id = db.Column(db.Integer,primary_key = True) #create columns using db.Column class which represents a single column.db.Integer specifies data to be stored
    username = db.Column(db.String(255)) #db.String class specifies data to be a string with 255 characters maximum

    def __repr__(self): #repr method easens debugging of our application
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.name}'