from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
def get_session():
    cloud_config= {
            'secure_connect_bundle': '<</PATH/TO/>>secure-connect-video-membership-project.zip'
    }
    auth_provider = PlainTextAuthProvider('<<CLIENT ID>>', '<<CLIENT SECRET>>')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()

    return session