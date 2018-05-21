
from flask_script import Manager,Server
from app import create_app,db #import db instance from app/__init__
from app.models import User,Comment,Pitch #import User class from app/models file

#Creating app instance          
app = create_app('development')

manager = Manager(app)

manager.add_command('server', Server)

@manager.shell #manage.shell decorator to create a shell context
def make_shell_context(): #make_shell_context function to pass in properties in our shell
    return dict(app = app,db = db,User = User,Comment = Comment,Pitch = Pitch) #return app application instance,db instance and User class

if __name__ == '__main__':
    manager.run()

