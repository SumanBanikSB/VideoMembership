from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cqlengine import connection
import pathlib

from . import config
BASE_DIR = pathlib.Path(__file__).resolve().parent # Gives the relative path of the current db folder...

settings = config.get_settings()

ASTRADB_CONNECT_BUNDLE = BASE_DIR / 'connect_bundle'/'astradb_connect.zip'
ASTRADB_CLIENT_ID = settings.db_client_id
ASTRADB_CLIENT_SECRET = settings.db_client_secret

def get_session():
    cloud_config= {
            'secure_connect_bundle': ASTRADB_CONNECT_BUNDLE
    }
    auth_provider = PlainTextAuthProvider(ASTRADB_CLIENT_ID, ASTRADB_CLIENT_SECRET)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    connection.register_connection(str(session), session=session)
    connection.set_default_connection(str(session))
    return session