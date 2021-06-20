from config import * ## config.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.dialects.postgresql import UUID
import os

from blueprints.path import path_blueprint

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.register_blueprint(path_blueprint, url_prefix='/path')


import models, routes ## models/ and routes.py
