import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db



# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
migrate = Migrate(app, db) # create a migration instance
manager = Manager(app) # manager instance

manager.add_command('db', MigrateCommand)
# db.create_all()
@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(
        username="admin",
        password="admin",
        admin=True,
        confirmed=True,
        confirmed_on=datetime.datetime.now())
    )
    db.session.commit()


if __name__=="__main__":
	manager.run()
