print("=== INICIANDO START.PY ===")
import os
import configparser
from waitress import serve
from contact import main
from contact.model import Base
from sqlalchemy import create_engine

config = configparser.ConfigParser()
config.read('development.ini')
settings = dict(config['app:main'])

database_url = os.environ.get('DATABASE_URL')
if database_url:
    settings['sqlalchemy.url'] = database_url

# Crear tablas automáticamente
engine = create_engine(settings['sqlalchemy.url'])
Base.metadata.create_all(engine)

app = main({}, **settings)
port = int(os.environ.get('PORT', 6543))
print(f'Serving on port {port}')
serve(app, host='0.0.0.0', port=port)
