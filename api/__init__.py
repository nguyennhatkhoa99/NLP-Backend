"""Flask SQLAlchemy"""
from dotenv import dotenv_values
from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import os
from importlib import import_module
from pathlib import Path

from flask_login import LoginManager
from flask_socketio import SocketIO, join_room, leave_room
from flask_bcrypt import Bcrypt

from config import Config

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin


app = Flask(__name__, instance_relative_config=True)
CORS(app, support_credentials=True)

app.config.from_object(Config)
login_manager = LoginManager()
Base = declarative_base()
url_object = URL.create(
    "postgresql",
    username=app.config['DB_USERNAME'],
    password=app.config['DB_PASSWORD'],
    host=app.config['DB_HOST'],
    database=app.config['DB_NAME'],
    port=app.config['DB_PORT']
)


engine = create_engine(url = "postgresql://postgres:khoa@postgres:5432/chat", echo=True)

session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)
Base.metadata.create_all(engine)
print('hello',Base.metadata)

@app.teardown_request
def shutdown_session(exception=None):
    session.remove()


def register_blueprint(app):
    root_folder = Path.cwd().absolute()
    api_folder = os.path.join(root_folder,'api')
    sub_api_folder = [name for name in os.listdir(api_folder) if os.path.isdir(os.path.join(api_folder, name))]
    for module_name in sub_api_folder:
        if module_name == '__pycache__':
            continue
        module = import_module('api.{}.route'.format(module_name))
        print(module.blueprint)
        app.register_blueprint(module.blueprint)

def create_app():
    from api.chat_room.model import ChatroomModel
    from api.form.model import FormModel
    from api.content_generator.model import ContentGeneratorModel
    from api.user.model import UserModel
    Base.metadata.create_all(engine)
    login_manager.init_app(app)
    with app.app_context():
        register_blueprint(app=app)
    return app