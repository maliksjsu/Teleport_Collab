# Set the path
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from chef_browser import app

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = os.getenv('IP', '0.0.0.0'), #host = '0.0.0.0',
    port = int(os.getenv('PORT', 5000)))#port = "5000")
)

if __name__ == "__main__":
    #host = os.getenv('IP', '0.0.0.0')
    #port = int(os.getenv('PORT', 5000))
    manager.run()
