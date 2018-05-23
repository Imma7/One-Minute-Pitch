import os #import os module that allows our app to interact with the OS dependent functionality

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://immanuel:7007@localhost/pitchdb'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}

config_options = {
'development':DevConfig,
'production':ProdConfig
}