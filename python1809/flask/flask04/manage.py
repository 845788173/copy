import os

from flask import Flask
from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

app=create_app(os.environ.get('Flask_Env')or 'default')


manager=Manager(app=app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
