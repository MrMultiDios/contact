import os
import configparser
from waitress import serve
from contact import main

config = configparser.ConfigParser()
config.read('development.ini')
settings = dict(config['app:main'])
app = main({}, **settings)
port = int(os.environ.get('PORT', 6543))
print(f'Serving on port {port}')
serve(app, host='0.0.0.0', port=port)
```
