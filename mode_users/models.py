from ..app import db
from sqlalchemy import Column , Integer , String

class userclass(db.Model):
    id = Column(Integer , primary_key=True )
    fullname = Column(String(60) , nullable=False , unique=False)
    email = Column(String(100) , nullable=False , unique=True)
    password = Column(String(32) , nullable=False , unique=False)
    role = Column(Integer(2) , nullable=True , default=0)