print("=== INICIANDO START.PY ===")
import os
import configparser
from waitress import serve
from contact import main

config = configparser.ConfigParser()
config.read('development.ini')
settings = dict(config['app:main'])

# Usar DATABASE_URL de Railway si existe
database_url = os.environ.get('DATABASE_URL')
if database_url:
    settings['sqlalchemy.url'] = database_url

app = main({}, **settings)
port = int(os.environ.get('PORT', 6543))
print(f'Serving on port {port}')
serve(app, host='0.0.0.0', port=port)
