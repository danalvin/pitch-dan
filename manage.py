from app import create_app,db
from flask_script import Manager, Shell, Server
from app.models import User,Role, Comment
from flask_migrate import Migrate, MigrateCommand

app = create_app ('development')
app = create_app ('test')

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.comand
def test():
    import unittest
    tests = unittest.Testloader().discover('tests')
    unitest.TestTestRunner(verbosity=3).run(tests)

@manager.Shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role )

if __name__== '__main__':
    manager.run()