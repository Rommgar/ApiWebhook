class BaseSettings(object):
    """
    Base settings for the application.
    """
    API_PREFIX_URL = '/api/v1/'
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'BaseSettingsSecretKey'


class DevelopmentSettings(BaseSettings):
    """
    Development settings for the application.
    """
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'DevelopmentSettingsSecretKey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/api.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_SQLALCHEMY_LOG_MESSAGES = False


class TestingSettings(BaseSettings):
    """
    Testing settings for the application.
    """
    ENV = 'testing'
    DEBUG = False
    TESTING = True
    SECRET_KEY = 'TestingSettingsSecretKey'


class ProductionSettings(BaseSettings):
    """
    Production settings for the application.
    """
    ENV = 'production'
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'ProductionSettingsSecretKey'