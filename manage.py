from app import create_app,db
from flask_script import Manager, Shell, Server
from app.models import User,Role, Comment
from flask_migrate import Migrate, MigrateCommand