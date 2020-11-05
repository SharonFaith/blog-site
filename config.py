import os

class Config:
    '''
    General configuration parent class
    '''
#   QUOTES_API_BASE_URL ='http://quotes.stormconsultancy.co.uk/random.json'

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:Amazeing16@localhost/blog_site'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
  #  UPLOADED_PHOTOS_DEST = 'app/static/photos'
   
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    #simple mde configurations
    #SIMPLEMDE_JS_IIFE = True
    #SIMPLEMDE_USE_CDN = True
    pass

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
#    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class TestConfig(Config):
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:Amazeing16@localhost/'
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
 #   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:Amazeing16@localhost/blog_site'
    
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig, 
    'test': TestConfig
}