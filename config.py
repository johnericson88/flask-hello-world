import os
SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = "sqlite:///database\\helloworld.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False