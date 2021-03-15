from sqlalchemy import create_engine
from os import getenv


env = getenv('ENV') or 'dev'

url = {
    'dev': 'sqlite:///local.db',
    'test': 'sqlite:///test.db',
}[env]

config = {
    'echo': False,
}

engine = create_engine(url, **config)
