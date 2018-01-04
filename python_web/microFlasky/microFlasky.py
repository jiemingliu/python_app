import os
from app import create_app,db
from app.models import User,Role
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand

import logging as logger
logger.basicConfig(level=logger.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)


@app.shell_context_processor
def make_shell_context():
	return dict(app=app,db=db,User=User,Role=Role)

manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
	manager.run()
	logger.info('start successfully')