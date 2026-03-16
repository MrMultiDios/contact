import os
import configparser
from wsgiref.simple_server import make_server
from contact import main as app_factory

config = configparser.ConfigParser()
config.read('development.ini')

settings = dict(config['app:main'])
settings['__file__'] = os.path.abspath('development.ini')

app = app_factory({}, **settings)

print('Servidor corriendo en http://localhost:6543')
server = make_server('localhost', 6543, app)
server.serve_forever()