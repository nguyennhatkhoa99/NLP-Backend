import os

basedir = os.path.abspath(os.path.dirname(__file__))
# print('{}://{}:{}@{}:{}/{}'.format(
#         os.getenv('DB_ENGINE'   , 'postgresql'),
#         os.getenv('DB_USERNAME' , 'postgres'),
#         os.getenv('DB_PASSWORD' , 'khoa'),
#         os.getenv('DB_HOST'     , 'localhost'),
#         os.getenv('DB_PORT'     , 5432),
#         os.getenv('DB_NAME'     , 'chat')
# ))
class Config(object):
    DEBUG = os.getenv("DEBUG") or False
    TESTING = os.getenv("TESTING") or False
    SECRET_KEY = os.getenv('SECRET_KEY') or 'secret-key'
    CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND") or "redis://localhost:6379"
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL") or "redis://localhost:6379"
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        os.getenv('DB_ENGINE'   , 'postgresql'),
        os.getenv('DB_USERNAME' , 'postgres'),
        os.getenv('DB_PASSWORD' , 'khoa'),
        os.getenv('DB_HOST'     , 'localhost'),
        os.getenv('DB_PORT'     , 5432),
        os.getenv('DB_NAME'     , 'chat')
    )
    DB_ENGINE   = os.getenv('DB_ENGINE'   , None)
    DB_USERNAME = os.getenv('DB_USERNAME' , None)
    DB_PASSWORD = os.getenv('DB_PASSWORD' , None)
    DB_HOST     = os.getenv('DB_HOST'     , None)
    DB_PORT     = os.getenv('DB_PORT'     , None)
    DB_NAME     = os.getenv('DB_NAME'     , None)
class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
