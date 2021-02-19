import os

class Database:
    NAME = os.getenv('POSTGRES_DB')
    USER = os.getenv('POSTGRES_USER')
    PASSWORD = os.getenv('POSTGRES_PASSWORD')
    HOST = os.getenv('DATABASE_HOST')
    PORT = os.getenv('DATABASE_PORT')

# SECURITY WARNING: keep the secret key used in production secret!
# Remember to replace this with your own secret key
class Secrets:
    SECRET_KEY = "_eq-(x@_&hyhnx9-u%&gy2k1)4es8jvu72#=y$)9mad-!q)tg+"
