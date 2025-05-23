import os 
class Config:
    SQLACLCHEMY_DATABASE_URI = 'mysql://root@localhost/hoteis'
    SQLACLCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    
    