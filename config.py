import os
from os import environ


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = environ.get('DB_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
