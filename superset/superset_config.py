import os

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://redis:6379/1'}
SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://superset:superset@postgres:5432/superset'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'thisISaSECRET_1234'


#MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', 'pk.eyJ1IjoibWFyY3VzcmIiLCJhIjoiY2twZjl3Nm5qMjUzNTJubmxpd2pmbG85MiJ9.alTxP9BebIMgLT8q_JZSmA')
# CACHE_CONFIG = {
#     'CACHE_TYPE': 'redis',
#     'CACHE_DEFAULT_TIMEOUT': 300,
#     'CACHE_KEY_PREFIX': 'superset_',
#     'CACHE_REDIS_HOST': 'redis',
#     'CACHE_REDIS_PORT': 6379,
#     'CACHE_REDIS_DB': 1,
#     'CACHE_REDIS_URL': 'redis://redis:6379/1'}

# POSTGRES_USER = os.getenv('POSTGRES_USER')
# POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
# POSTGRES_HOST = os.getenv('POSTGRES_HOST')
# #POSTGRES_PORT = int(os.getenv('POSTGRES_PORT', '5432'))
# POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE')
# POSTGRES_USER=pguser
# POSTGRES_PASSWORD=pgpassword
# # POSTGRES_HOST=dev-tfm-uoc.southcentralus.cloudapp.azure.com
# POSTGRES_HOST=dev-tfm-uoc.southcentralus.cloudapp.azure.com
# POSTGRES_PORT=5432
# POSTGRES_DATABASE=pguser


# SQLALCHEMY_DATABASE_URI = \
#     'postgresql+psycopg2://{0}:{1}@{2}:5432/{4}'.format(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_DATABASE)
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SECRET_KEY = 'thisISaSECRET_1234'
