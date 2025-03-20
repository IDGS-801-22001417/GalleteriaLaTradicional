import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = 'Clave nueva'
    SESSION_COOKIE_SECRET = False
    
class DeveplopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:oagl@127.0.0.1/DonLandin'
    SQLALCHEMY_TRACK_MODIFICATIONS = False