from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db
import os


app.config.from_object(os.environ['APP_SETTINGS']) # application configuration

migrate = Migrate(app, db) # create a migration instance
manager = Manager(app) # manager instance

manager.add_command('db', MigrateCommand)


if __name__=="__main__":
    manager.run(debug=True)
