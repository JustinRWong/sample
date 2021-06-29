from config import * ## config.py
from flask import Flask
import os

from blueprints.path import path_blueprint

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app.register_blueprint(path_blueprint, url_prefix='/path')


import routes ## and routes.py
