import os #import os module that allows our app to interact with the OS dependent functionality

class Config:
    
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = os.urandom(24)
    
    # WTF_CSRF_SECRET_KEY="a csrf secret key"



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://immanuel:7007@localhost/pitchdb'
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}

config_options = {
'development':DevConfig,
'production':ProdConfig
}