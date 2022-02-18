# Database with cassandra with class

from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
import uuid
from app.config import get_settings
# uuid1 gives a timestamp value, important for a lot of users.
settings = get_settings()

class User(Model):
    __keyspace__ = settings.keyspace
    email = columns.Text(primary_key = True)
    user_id = columns.UUID(primary_key = True,default = uuid.uuid1)
    password = columns.Text()

    def __str__(self):
        return self.__repr__()

    def __repr__(self): # Representation of the class
        return f"User(email = {self.email},user_id = {self.user_id})"
